from test.test_cases import test_cases
from colorama import Fore, Style, init

# Initialize colorama for Windows
init(autoreset=True)

class TestResult:
    def __init__(self):
        self.passed = 0
        self.failed = 0
        self.errors = 0
        self.results = []

    def add_result(self, query, expected, actual, status, error_msg=None):
        self.results.append({
            'query': query,
            'expected': expected,
            'actual': actual,
            'status': status,
            'error': error_msg
        })
        if status == 'PASS': self.passed += 1
        elif status == 'FAIL': self.failed += 1
        else: self.errors += 1

def run_tests(calculator, tolerance=1e-9):
    results = TestResult()
    for query, expected in test_cases:
        try:
            actual = calculator.evaluate(query)
            if abs(actual - expected) < tolerance:
                results.add_result(query, expected, actual, 'PASS')
            else:
                results.add_result(query, expected, actual, 'FAIL')
        except Exception as e:
            results.add_result(query, expected, None, 'ERROR', str(e))
    return results

def print_results(results: TestResult):
    print("\n" + "=" * 60)
    print(Fore.CYAN + Style.BRIGHT + " TEST RESULTS ".center(60, "="))
    print("=" * 60)

    # Detailed results
    for i, res in enumerate(results.results, 1):
        status_color = {
            'PASS': Fore.GREEN,
            'FAIL': Fore.RED,
            'ERROR': Fore.YELLOW
        }[res['status']]

        print(f"{status_color}{res['status']:<6}{Style.RESET_ALL} | "
              f"Case {i:02d}: {res['query']}")
        print(f"       Expected: {res['expected']}  |  Got: {res['actual']}")
        if res['error']:
            print(f"       {Fore.YELLOW}Error: {res['error']}{Style.RESET_ALL}")
        print("-" * 60)
    print(
        f"{Fore.GREEN}✔ Passed: {results.passed}  "
        f"{Fore.RED}✘ Failed: {results.failed}  "
        f"{Fore.YELLOW}! Errors: {results.errors}"
    )
    print("-" * 60)
