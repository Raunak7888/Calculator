# Not a Basic Calculator 🚀

<div align="center">

![Status](https://img.shields.io/badge/Status-Having%20Fun-ff69b4?style=for-the-badge)
![Vibes](https://img.shields.io/badge/Vibes-Immaculate-brightgreen?style=for-the-badge)
![Math](https://img.shields.io/badge/Math-Actually%20Works-blue?style=for-the-badge)

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

**Basically:** We're peeking under the hood of something you use every day!

---

## 🎪 Cool Tricks It Can Do

### The Basics (But Cooler)

- [x] **Addition** (`+`) - Your bread and butter
- [x] **Subtraction** (`−`) - When you owe your friend money
- [x] **Multiplication** (`×`) - Rabbits, basically
- [x] **Division** (`÷`) - Sharing pizza (with math!)
- [x] **Modulus** (`%`) - The "what's left over?" operator

### Power Moves 💪

- [x] **Exponents** (`^`) - Because `2^10` is easier than writing `2*2*2*2*2*2*2*2*2*2`
- [x] **Square** (`x²`) - The OG power move
- [x] **Cube** (`x³`) - Like square but... more
- [x] **Square root** (`√x`) - Reverse psychology for squares
- [x] **Cube root** (`∛x`) - Even more reverse psychology
- [x] **n-th root** - When you're feeling fancy
- [x] **Reciprocal** (`1/x`) - Flip it and reverse it!

### Exponential & Log Stuff (For When You Feel Like a Scientist) 📈

- [ ] `e^x` - The exponential function (nature's favorite)
- [ ] `10^x` - Scientific notation's best friend
- [ ] `ln x` - Natural log (sounds fancy, is fancy)
- [ ] `log₁₀ x` - What your calculator button actually does
- [ ] `logₐ x` - Choose your own adventure log!

### Trigonometry Time! 📐

- [ ] `sin`, `cos`, `tan` - The holy trinity of triangles
- [ ] `csc`, `sec`, `cot` - The cool cousins nobody talks about
- [ ] Degrees, radians, and grads - because why have one unit when you can have three?

### Inverse Trig (Going Backwards!) ↩️

- [ ] `arcsin`, `arccos`, `arctan` - Uno reverse card for trig
- [ ] All the inverses of those cool cousins too

### Hyperbolic Functions (Trig's Weird Sibling)

- [ ] `sinh`, `cosh`, `tanh` - Like trig but... hyperbolic?
- [ ] `csch`, `sech`, `coth` - The extended family
- [ ] All their inverses - because symmetry is beautiful

### Factorial & Friends 🎲

- [ ] `n!` - The exclamation point that means multiply everything
- [ ] `nPr` - Permutations (order matters!)
- [ ] `nCr` - Combinations (order doesn't matter!)

### The Special Numbers Club 🎩

- [ ] `π` - Circle's favorite constant
- [ ] `e` - Euler's number (irrational and proud!)
- [ ] `Ans` - Remember what you just calculated
- [ ] Memory buttons (`M+`, `M−`, `MR`, `MC`) - Like copy-paste for numbers

### Utility Belt 🦸

- [ ] `|x|` - Absolute value (always positive vibes)
- [ ] `⌊x⌋` - Floor (round down, always)
- [ ] `⌈x⌉` - Ceiling (round up, always)
- [ ] `Rand` - When you need chaos in your calculations
- [ ] Percentage calculations
- [ ] Scientific notation (for really big or tiny numbers)
- [ ] Unit conversions (degrees ↔ radians, polar ↔ rectangular, etc.)

### Secret Sauce 🌶️

- Handles **negative numbers** like a boss
- Understands **implicit multiplication**: `2(3+4)` = `2*(3+4)`
- Respects **parentheses** - no rebellion here!
- Doesn't explode when you try `5/0` (it just politely refuses)

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

---

## 🎮 How To Play

```python
from calculator import StackQueueCalculator

calc = StackQueueCalculator()

# Basic stuff
calc.evaluate("2 + 2")  # 4 (calculator confirms you can count!)

# Getting fancy
calc.evaluate("(5 + 3) * 2^3")  # 64 (look at you go!)

# Implicit multiplication magic
calc.evaluate("5(2 + 3)")  # 25 (no * needed!)

# Negative vibes
calc.evaluate("-10 + 5")  # -5 (math still works when sad)

# Going wild
calc.evaluate("2^(3^2)")  # 512 (POWER TOWER!)
```

---

## 🏗️ Under The Hood (Without Getting Too Nerdy)

```text
Your Math → [Tokenizer] → [Add Magic] → [Shunting Yard] → [Stack Go Brr] → Answer!
              ↓              ↓              ↓                    ↓
           "Break it"    "Fix it"      "Sort it"           "Solve it"
```

**The Journey:**

1. **Tokenizer**: Breaks your string into pieces (numbers and operators)
2. **Implicit Multiplication**: Adds missing `*` symbols (we're helpful like that)
3. **Shunting Yard**: Rearranges everything into RPN (computer-friendly format)
4. **Stack Evaluator**: Crunches the numbers and spits out an answer

---

## 🎨 Why This Is Actually Cool

- **Zero dependencies** - Just you, Python, and the power of algorithms
- **See how compilers work** - Same techniques used in real programming languages!
- **Learn data structures** - Stacks, queues, and trees in action
- **Build something tangible** - Not just theory, it actually calculates!
- **Easy to experiment** - Add your own operators and functions
- **Break things safely** - Try to break it! Learn from error messages!

---

## 🤝 Want To Join The Fun?

Jump in! Some ideas:

- 🎯 Try implementing one of the unchecked features
- 🐛 Find bugs (there's probably some weird edge case)
- 📚 Add more examples
- 🎨 Make the error messages funnier
- 🧪 Write test cases for weird inputs
- 📖 Explain a concept you just learned

**No contribution is too small!** Even fixing a typo helps.

---

## 💡 Learning Resources

Want to dive deeper?

- **Shunting Yard Algorithm**: [Wikipedia](https://en.wikipedia.org/wiki/Shunting-yard_algorithm)
- **Reverse Polish Notation**: [Wikipedia](https://en.wikipedia.org/wiki/Reverse_Polish_notation)
- **Abstract Syntax Trees**: The next level of parsing
- **Operator Precedence**: Why math has rules

---

## 🎉 Credits

Built while learning about:

- Parsing and lexical analysis
- Algorithm design
- Stack-based computation
- How programming languages work

Inspired by curiosity and too much coffee ☕

---

<div align="center">

### 🌟 If you learned something, give it a star! 🌟

**Remember: Every expert was once a beginner who didn't give up!**

*Now go break things and learn stuff!* 🚀

</div>
