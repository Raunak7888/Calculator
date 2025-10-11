
from calculator.stack_queue_calc import StackQueueCalculator
from test.calculator_tester import print_results, run_tests


if __name__ == "__main__":
    calc = StackQueueCalculator()
    results = run_tests(calc)
    print_results(results)
