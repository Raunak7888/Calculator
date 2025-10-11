# Not a Basic Calculator 🚀

<div align="center">

![Status](https://img.shields.io/badge/Status-Feature%20Complete-ff69b4?style=for-the-badge)
![Vibes](https://img.shields.io/badge/Vibes-Immaculate-brightgreen?style=for-the-badge)
![Math](https://img.shields.io/badge/Math-Actually%20Works-blue?style=for-the-badge)
![Functions](https://img.shields.io/badge/Functions-50+-orange?style=for-the-badge)

**Because learning algorithms shouldn't feel like homework!**

A fun way to explore data structures, parsing algorithms, and how computers actually do math

</div>

---

## 🤔 What Even Is This?

Ever wondered how your professional calculator app actually works? Or how programming languages understand `2 + 3 * 4` and know to multiply first? Well, buckle up!

This is a **learning project** where we're building a calculator from scratch to understand:

- 🧩 How to parse text into meaningful tokens
- 🎯 How operator precedence works (PEMDAS, anyone?)
- 🥞 How stacks and queues make everything easier
- 🔄 What the heck "Reverse Polish Notation" means (spoiler: it's pretty cool!)
- 🎨 How to structure code so adding new features doesn't break everything
- 🧪 Clean Code principles in action
- 🛠️ Pragmatic programming patterns

**Basically:** We're peeking under the hood of something you use every day!

---

## 🎪 Cool Tricks It Can Do

### The Basics (But Cooler)

- ✅ **Addition** (`+`) - Your bread and butter
- ✅ **Subtraction** (`−`) - When you owe your friend money
- ✅ **Multiplication** (`×`) - Rabbits, basically
- ✅ **Division** (`÷`) - Sharing pizza (with math!)
- ✅ **Modulus** (`%`) - The "what's left over?" operator

### Power Moves 💪

- ✅ **Exponents** (`^`) - Because `2^10` is easier than writing `2*2*2*2*2*2*2*2*2*2`
- ✅ **Square root** (`sqrt(x)`) - Reverse psychology for squares
- ✅ **Cube root** (`cbrt(x)`) - Even more reverse psychology
- ✅ **n-th root** (`nrt(x, n)`) - When you're feeling fancy: `nrt(32, 5)` = 2
- ✅ **Reciprocal** (`recip(x)`) - Flip it and reverse it!
- ✅ **Power function** (`pow(x, y)`) - Alternative to `^`

### Exponential & Log Stuff (For When You Feel Like a Scientist) 📈

- ✅ `e(x)` - The exponential function (nature's favorite): e^x
- ✅ `exp10(x)` - Scientific notation's best friend: 10^x
- ✅ `ln(x)` - Natural log (sounds fancy, is fancy)
- ✅ `log(x)` - Base-10 logarithm (what your calculator button actually does)
- ✅ `log2(x)` - Binary logarithm (for computer science nerds)
- ✅ `logb(x, base)` - Choose your own adventure log! `logb(8, 2)` = 3

### Trigonometry Time! 📐

- ✅ `sin(x)`, `cos(x)`, `tan(x)` - The holy trinity of triangles
- ✅ `csc(x)`, `sec(x)`, `cot(x)` - The cool cousins nobody talks about
- ✅ `rad(x)` - Convert degrees to radians
- ✅ `deg(x)` - Convert radians to degrees

### Inverse Trig (Going Backwards!) ↩️

- ✅ `asin(x)`, `acos(x)`, `atan(x)` - Uno reverse card for trig
- ✅ `acsc(x)`, `asec(x)`, `acot(x)` - All the inverses of those cool cousins too
- ✅ `atan2(y, x)` - Two-argument arctangent (for proper quadrant handling)

### Hyperbolic Functions (Trig's Weird Sibling)

- ✅ `sinh(x)`, `cosh(x)`, `tanh(x)` - Like trig but... hyperbolic?
- ✅ `csch(x)`, `sech(x)`, `coth(x)` - The extended family
- ✅ `asinh(x)`, `acosh(x)`, `atanh(x)` - All their inverses (because symmetry is beautiful)
- ✅ `acsch(x)`, `asech(x)`, `acoth(x)` - The complete inverse collection

### Factorial & Friends 🎲

- ✅ `fact(n)` - The exclamation point that means multiply everything (with overflow protection!)
- ✅ `nPr(n, r)` - Permutations (order matters!) - `nPr(5, 2)` = 20
- ✅ `nCr(n, r)` - Combinations (order doesn't matter!) - `nCr(5, 2)` = 10
- ✅ `gcd(a, b)` - Greatest common divisor
- ✅ `lcm(a, b)` - Least common multiple

### The Special Numbers Club 🎩

- ✅ `π` or `pi` - Circle's favorite constant (3.14159...)
- ✅ `e` - Euler's number (2.71828... irrational and proud!)
- ✅ `tau` - The superior circle constant (2π, fight me)
- ✅ `phi` - The golden ratio (1.618...)
- ✅ `ans` - Remember what you just calculated (auto-updates!)

### Utility Belt 🦸

- ✅ `abs(x)` - Absolute value (always positive vibes)
- ✅ `floor(x)` - Floor (round down, always)
- ✅ `ceil(x)` - Ceiling (round up, always)
- ✅ `round(x)` - Round to nearest integer
- ✅ `trunc(x)` - Truncate decimal part
- ✅ `sign(x)` - Sign function (-1, 0, or 1)
- ✅ `rand(x)` - Random number generator [0, 1) (x is ignored)
- ✅ `hypot(x, y)` - Hypotenuse: sqrt(x² + y²)

### Memory Features 🧠

- ✅ `M+` - Memory add
- ✅ `M-` - Memory subtract  
- ✅ `MR` - Memory recall
- ✅ `MC` - Memory clear
- ✅ `ans` - Last answer (automatically stored)

### Secret Sauce 🌶️

- Handles **negative numbers** like a boss: `-5 + 3` works perfectly
- Understands **implicit multiplication**: `2(3+4)` = `2*(3+4)`, `2pi` = `2*π`
- Respects **parentheses** - no rebellion here!
- Doesn't explode when you try `5/0` (it just politely refuses)
- **Domain checking** - Won't let you `sqrt(-1)` (we're staying real here)
- **Overflow protection** - `fact(200)` will warn you instead of crashing
- **Binary functions** - `nPr(5, 2)` and `logb(8, 2)` with comma-separated args

---

## 🎓 What You'll Learn

By poking around this project, you'll discover:

### The Secret Sauce of Parsing

```text
"2 + 3 * 4"  →  [2, '+', 3, '*', 4]  →  [2, 3, 4, '*', '+']  →  14
   (Input)         (Tokens)           (Reverse Polish)      (Magic!)
```

### The Shunting Yard Algorithm 🚂

Imagine organizing trains in a rail yard. That's literally what this algorithm does with your math! It figures out what order to do operations by shuffling operators around using a stack.

### Stack-Based Evaluation 🥞

Everything gets solved using a stack (like a stack of pancakes, but with numbers). Pop, calculate, push. Repeat until you have breakfast... er, an answer!

### Clean Code Principles 📚

- **Single Responsibility**: Each function does ONE thing well
- **Descriptive Naming**: `_safe_sqrt()` vs `sqrt()` makes intent crystal clear
- **Error Handling**: Comprehensive validation with helpful error messages
- **DRY (Don't Repeat Yourself)**: Reusable helper functions
- **Type Hints**: For better IDE support and code clarity
- **Documentation**: Clear docstrings for public APIs

### Pragmatic Programming 🛠️

- **Separation of Concerns**: Tokenization → Parsing → Evaluation
- **Extensibility**: Adding new functions is just adding to a dictionary!
- **Fail Fast**: Catch errors early with domain validation
- **Test-Driven Thinking**: Comprehensive test suite with edge cases

---

## 🎮 How To Play

```python
from calculator import StackQueueCalculator

calc = StackQueueCalculator()

# ========== Basic Stuff ==========
calc.evaluate("2 + 2")                    # 4 (calculator confirms you can count!)
calc.evaluate("(5 + 3) * 2^3")            # 64 (look at you go!)

# ========== Implicit Multiplication Magic ==========
calc.evaluate("5(2 + 3)")                 # 25 (no * needed!)
calc.evaluate("2pi")                      # 6.283... (tau, basically)
calc.evaluate("2sqrt(16)")                # 8 (clean and simple)

# ========== Negative Vibes ==========
calc.evaluate("-10 + 5")                  # -5 (math still works when sad)
calc.evaluate("abs(-42)")                 # 42 (positive vibes only)

# ========== Power Tower ==========
calc.evaluate("2^(3^2)")                  # 512 (POWER TOWER!)
calc.evaluate("sqrt(16)")                 # 4
calc.evaluate("cbrt(27)")                 # 3
calc.evaluate("nrt(32, 5)")               # 2 (5th root of 32)

# ========== Science Mode Activated 🔬 ==========
calc.evaluate("e")                        # 2.718... (hello Euler!)
calc.evaluate("ln(e(5))")                 # 5 (logs and exponentials are friends)
calc.evaluate("log(100)")                 # 2 (base 10)
calc.evaluate("logb(8, 2)")               # 3 (log base 2 of 8)

# ========== Trigonometry Playground 📐 ==========
calc.evaluate("sin(0)")                   # 0
calc.evaluate("cos(0)")                   # 1
calc.evaluate("tan(rad(45))")             # 1 (45° in radians)
calc.evaluate("asin(0.5)")                # 0.523... (30° in radians)

# ========== Hyperbolic Zone 🌀 ==========
calc.evaluate("sinh(0)")                  # 0
calc.evaluate("cosh(0)")                  # 1
calc.evaluate("asinh(sinh(5))")           # 5 (round trip!)

# ========== Combinatorics Party 🎲 ==========
calc.evaluate("fact(5)")                  # 120 (5! = 5*4*3*2*1)
calc.evaluate("nPr(5, 2)")                # 20 (permutations)
calc.evaluate("nCr(5, 2)")                # 10 (combinations)

# ========== Advanced Wizardry 🧙 ==========
calc.evaluate("hypot(3, 4)")              # 5 (Pythagorean theorem!)
calc.evaluate("atan2(1, 1)")              # 0.785... (45° in radians)
calc.evaluate("gcd(48, 18)")              # 6
calc.evaluate("lcm(12, 18)")              # 36

# ========== Complex Expressions ==========
calc.evaluate("sqrt(3^2 + 4^2)")          # 5 (distance formula)
calc.evaluate("sin(pi/6)^2 + cos(pi/6)^2") # 1 (trig identity)
calc.evaluate("floor(3.9) + ceil(2.1)")   # 7

# ========== Memory Features ==========
result = calc.evaluate("5 * 10")          # 50
calc.memory_add(result)                   # M+ (adds 50 to memory)
calc.evaluate("20")                       # 20
calc.memory_add(20)                       # M+ (memory now has 70)
calc.memory_recall()                      # MR (returns 70)
calc.memory_clear()                       # MC (memory back to 0)

# ========== Using Last Answer ==========
calc.evaluate("10 + 5")                   # 15
calc.evaluate("ans * 2")                  # 30 (uses last answer)
```

---

## 🏗️ Under The Hood (Without Getting Too Nerdy)

```text
Your Math → [Tokenizer] → [Add Magic] → [Shunting Yard] → [Stack Go Brr] → Answer!
              ↓              ↓              ↓                    ↓
           "Break it"    "Fix it"      "Sort it"           "Solve it"
```

**The Journey:**

1. **Tokenizer**: Breaks your string into pieces (numbers, operators, functions, constants)
2. **Implicit Multiplication**: Adds missing `*` symbols (we're helpful like that)
3. **Shunting Yard**: Rearranges everything into RPN (computer-friendly format)
4. **Stack Evaluator**: Crunches the numbers and spits out an answer

### Architecture Highlights 🏛️

```python
StackQueueCalculator
├── Unary Functions (50+ functions)
│   ├── Trigonometric (sin, cos, tan, csc, sec, cot)
│   ├── Inverse Trig (asin, acos, atan, acsc, asec, acot)
│   ├── Hyperbolic (sinh, cosh, tanh, csch, sech, coth)
│   ├── Inverse Hyperbolic (asinh, acosh, atanh, acsch, asech, acoth)
│   ├── Logarithmic (ln, log, log2, e, exp10)
│   ├── Roots (sqrt, cbrt, recip)
│   └── Utility (abs, floor, ceil, round, trunc, sign, fact, rand)
│
├── Binary Functions (10+ functions)
│   ├── Statistical (nPr, nCr)
│   ├── Logarithmic (logb)
│   ├── Roots (nrt)
│   ├── Geometry (atan2, hypot)
│   └── Number Theory (gcd, lcm, pow)
│
├── Constants (5 constants)
│   ├── π (pi), e, tau, phi, ans
│
├── Memory System
│   ├── M+, M-, MR, MC
│   └── Last Answer (ans)
│
└── Smart Features
    ├── Domain Validation (no sqrt(-1))
    ├── Overflow Protection (fact(171) warns you)
    ├── Zero Division Handling
    ├── Implicit Multiplication
    └── Nested Function Support
```

---

## 🎨 Why This Is Actually Cool

- ✨ **50+ Functions** - From basics to advanced math
- 🛡️ **Bullet-proof** - Comprehensive error handling and domain checking
- 🎯 **Zero dependencies** - Just you, Python, and the power of algorithms
- 🔍 **See how compilers work** - Same techniques used in real programming languages!
- 📚 **Learn data structures** - Stacks, queues, and trees in action
- 🔧 **Build something tangible** - Not just theory, it actually calculates!
- 🚀 **Easy to experiment** - Add your own operators and functions
- 💣 **Break things safely** - Try to break it! Learn from error messages!
- 📖 **Clean Code showcase** - Production-ready code organization
- 🧪 **Test-friendly** - Comprehensive test suite included

---

## 🧪 Testing

Run the comprehensive test suite with 100+ test cases:

```bash
uv run calculator.py
```

Test categories:

- ✅ Basic arithmetic operations
- ✅ Unary and binary functions
- ✅ Nested function calls
- ✅ Implicit multiplication
- ✅ Negative numbers
- ✅ Edge cases and error conditions
- ✅ Complex real-world expressions
- ✅ Domain validation
- ✅ Overflow protection

---

## 🤝 Want To Join The Fun?

Jump in! Some ideas:

- 🎯 Add percentage calculations (`50% of 200`)
- 🔢 Implement scientific notation (`1.5e10`)
- 🎨 Create a GUI or CLI interface
- 📊 Add statistical functions (mean, median, variance)
- 🌐 Unit conversions (temperature, distance, etc.)
- 🧪 More test cases for weird inputs
- 📖 Tutorial blog posts explaining the algorithms
- 🎬 Video walkthrough of the code
- 🐛 Find edge cases we missed

**No contribution is too small!** Even fixing a typo helps.

---

## 💡 Learning Resources

Want to dive deeper?

- **Shunting Yard Algorithm**: [Wikipedia](https://en.wikipedia.org/wiki/Shunting-yard_algorithm)
- **Reverse Polish Notation**: [Wikipedia](https://en.wikipedia.org/wiki/Reverse_Polish_notation)
- **Clean Code**: Robert C. Martin's book
- **The Pragmatic Programmer**: Hunt & Thomas
- **Abstract Syntax Trees**: The next level of parsing
- **Operator Precedence**: [Wikipedia](https://en.wikipedia.org/wiki/Order_of_operations)

---

## 🎉 Credits

Built while learning about:

- Parsing and lexical analysis
- Algorithm design (Shunting Yard, Stack Evaluation)
- Stack-based computation
- How programming languages work
- Clean Code principles
- Pragmatic programming patterns
- Test-driven development

Inspired by curiosity, too much coffee ☕, and a desire to understand how things *really* work!

---

## 📊 Project Stats

- **Total Functions**: 50+
- **Lines of Code**: ~600 (clean and documented)
- **Test Cases**: 100+
- **Supported Operations**: 70+
- **Constants**: 5
- **Error Types Handled**: 10+

---

### 🌟 If you learned something, give it a star! 🌟

**Remember: Every expert was once a beginner who didn't give up!**

Made with 💖, 🧠, and probably too much ☕

*Now go break things and learn stuff!* 🚀

---

**Fun Fact**: This calculator can evaluate expressions like `sqrt(abs(sin(pi/4)^2 + cos(pi/4)^2))` and will correctly return `1.0`. Try it! 🎯
