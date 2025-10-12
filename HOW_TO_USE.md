# 🧮 How to Use the Calculator — Quick Reference

This is your **complete usage guide** for every operator, function, and constant supported by the calculator.
Just type expressions like:

```python
calc.evaluate("2 + 3 * sqrt(16)")
```

---

## ⚙️ **Operators**

| Operator | Description              | Example       | Result |
| -------- | ------------------------ | ------------- | ------ |
| `+`      | Addition                 | `2 + 3`       | `5`    |
| `-`      | Subtraction              | `5 - 2`       | `3`    |
| `*`      | Multiplication           | `4 * 5`       | `20`   |
| `/`      | Division                 | `10 / 2`      | `5`    |
| `%`      | Modulus (remainder)      | `10 % 3`      | `1`    |
| `^`      | Power (exponent)         | `2 ^ 3`       | `8`    |
| `()`     | Parentheses for grouping | `(2 + 3) * 4` | `20`   |

> 💡 **Implicit multiplication** works:
> `2pi`, `2(3+4)`, or `3sqrt(9)` are all valid.

---

## 🔢 **Constants**

| Constant   | Description            | Value            |
| ---------- | ---------------------- | ---------------- |
| `pi` or `` | Circle constant        | 3.1415926535     |
| `e`        | Euler’s number         | 2.7182818284     |
| `tau`      | 2 × π                  | 6.283185307      |
| `phi`      | Golden ratio           | 1.6180339887     |
| `ans`      | Last calculated result | — (auto updates) |

---

## 🧩 **Basic Math Functions**

| Function    | Example      | Result | Description      |
| ----------- | ------------ | ------ | ---------------- |
| `sqrt(x)`   | `sqrt(16)`   | 4      | Square root      |
| `cbrt(x)`   | `cbrt(27)`   | 3      | Cube root        |
| `nrt(x, n)` | `nrt(32, 5)` | 2      | n-th root        |
| `recip(x)`  | `recip(4)`   | 0.25   | Reciprocal (1/x) |
| `pow(x, y)` | `pow(2, 10)` | 1024   | x raised to y    |

---

## 📈 **Exponential & Logarithmic**

| Function        | Example       | Result | Description       |
| --------------- | ------------- | ------ | ----------------- |
| `e(x)`          | `e(2)`        | 7.389  | e^x               |
| `exp10(x)`      | `exp10(3)`    | 1000   | 10^x              |
| `ln(x)`         | `ln(e(5))`    | 5      | Natural logarithm |
| `log(x)`        | `log(100)`    | 2      | Base-10 log       |
| `log2(x)`       | `log2(8)`     | 3      | Base-2 log        |
| `logb(x, base)` | `logb(81, 3)` | 4      | Log base `base`   |

---

## 📐 **Trigonometric**

| Function | Example             | Description       |
| -------- | ------------------- | ----------------- |
| `sin(x)` | `sin(pi/2)` → 1     | Sine              |
| `cos(x)` | `cos(0)` → 1        | Cosine            |
| `tan(x)` | `tan(pi/4)` → 1     | Tangent           |
| `csc(x)` | `csc(pi/2)` → 1     | Cosecant          |
| `sec(x)` | `sec(0)` → 1        | Secant            |
| `cot(x)` | `cot(pi/4)` → 1     | Cotangent         |
| `rad(x)` | `rad(180)` → 3.1415 | Degrees → Radians |
| `deg(x)` | `deg(pi)` → 180     | Radians → Degrees |

---

## 🔄 **Inverse Trigonometric**

| Function      | Example       | Description           |
| ------------- | ------------- | --------------------- |
| `asin(x)`     | `asin(0.5)`   | Inverse sine          |
| `acos(x)`     | `acos(0.5)`   | Inverse cosine        |
| `atan(x)`     | `atan(1)`     | Inverse tangent       |
| `acsc(x)`     | `acsc(2)`     | Inverse cosecant      |
| `asec(x)`     | `asec(2)`     | Inverse secant        |
| `acot(x)`     | `acot(1)`     | Inverse cotangent     |
| `atan2(y, x)` | `atan2(1, 1)` | 2-argument arctangent |

---

## 🌊 **Hyperbolic Functions**

| Function  | Example       | Description          |
| --------- | ------------- | -------------------- |
| `sinh(x)` | `sinh(0)` → 0 | Hyperbolic sine      |
| `cosh(x)` | `cosh(0)` → 1 | Hyperbolic cosine    |
| `tanh(x)` | `tanh(1)`     | Hyperbolic tangent   |
| `csch(x)` | `csch(1)`     | Hyperbolic cosecant  |
| `sech(x)` | `sech(1)`     | Hyperbolic secant    |
| `coth(x)` | `coth(1)`     | Hyperbolic cotangent |

---

## ♾️ **Inverse Hyperbolic**

| Function   | Example      | Description                  |
| ---------- | ------------ | ---------------------------- |
| `asinh(x)` | `asinh(1)`   | Inverse hyperbolic sine      |
| `acosh(x)` | `acosh(2)`   | Inverse hyperbolic cosine    |
| `atanh(x)` | `atanh(0.5)` | Inverse hyperbolic tangent   |
| `acsch(x)` | `acsch(2)`   | Inverse hyperbolic cosecant  |
| `asech(x)` | `asech(0.5)` | Inverse hyperbolic secant    |
| `acoth(x)` | `acoth(2)`   | Inverse hyperbolic cotangent |

---

## 🎲 **Utility Functions**

| Function   | Example      | Result     | Description         |
| ---------- | ------------ | ---------- | ------------------- |
| `abs(x)`   | `abs(-10)`   | 10         | Absolute value      |
| `floor(x)` | `floor(3.9)` | 3          | Round down          |
| `ceil(x)`  | `ceil(3.1)`  | 4          | Round up            |
| `round(x)` | `round(3.6)` | 4          | Round to nearest    |
| `trunc(x)` | `trunc(3.9)` | 3          | Remove decimal part |
| `sign(x)`  | `sign(-8)`   | -1         | Sign of number      |
| `rand(x)`  | `rand(0)`    | Random 0–1 | Random number       |

---

## 🔢 **Combinatorics & Number Theory**

| Function      | Example       | Result | Description             |
| ------------- | ------------- | ------ | ----------------------- |
| `fact(n)`     | `fact(5)`     | 120    | Factorial (n!)          |
| `nPr(n, r)`   | `nPr(5, 2)`   | 20     | Permutations            |
| `nCr(n, r)`   | `nCr(5, 2)`   | 10     | Combinations            |
| `gcd(a, b)`   | `gcd(48, 18)` | 6      | Greatest common divisor |
| `lcm(a, b)`   | `lcm(12, 18)` | 36     | Least common multiple   |
| `hypot(x, y)` | `hypot(3, 4)` | 5      | Hypotenuse (Pythagoras) |

---

## 💾 **Memory Functions**

| Command              | Example                    | Description               |
| -------------------- | -------------------------- | ------------------------- |
| `memory_add(x)`      | `calc.memory_add(50)`      | Add to memory (M+)        |
| `memory_subtract(x)` | `calc.memory_subtract(20)` | Subtract from memory (M-) |
| `memory_recall()`    | `calc.memory_recall()`     | Recall stored value (MR)  |
| `memory_clear()`     | `calc.memory_clear()`      | Clear memory (MC)         |
| `ans`                | Used in equation           | Last answer               |

---

## 🧩 **Special Behavior**

✅ Handles **negative numbers** → `-5 + 3`
✅ Supports **implicit multiplication** → `2pi`, `5(2+3)`
✅ Understands **nested functions** → `sqrt(abs(-9))`
✅ Smart error messages for invalid domains
