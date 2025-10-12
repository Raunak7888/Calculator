# 🧮 How to Use the Calculator — Quick Reference

This is your **complete usage guide** for every operator, function, and constant supported by the calculator.
Just type expressions like:

```python
calc.evaluate("2 + 3 * sqrt(16)")
```

---

## ⚙️ **Operators**

| Operator | Example       | Result | Description              |
| -------- | ------------- | ------ | ------------------------ |
| `+`      | `2 + 3`       | 5      | Addition                 |
| `-`      | `5 - 2`       | 3      | Subtraction              |
| `*`      | `4 * 5`       | 20     | Multiplication           |
| `/`      | `10 / 2`      | 5      | Division                 |
| `%`      | `10 % 3`      | 1      | Modulus (remainder)      |
| `^`      | `2 ^ 3`       | 8      | Power (exponent)         |
| `()`     | `(2 + 3) * 4` | 20     | Parentheses for grouping |

> 💡 **Implicit multiplication** works:
> `2pi`, `2(3+4)`, or `3sqrt(9)` are all valid.

---

## 🔢 **Constants**

| Constant   | Example   | Result        | Description            |
| ---------- | --------- | ------------- | ---------------------- |
| `pi` or `` | `2pi`     | 6.283185307   | Circle constant        |
| `e`        | `e`       | 2.7182818284  | Euler’s number         |
| `tau`      | `tau`     | 6.283185307   | 2 × π                  |
| `phi`      | `phi`     | 1.6180339887  | Golden ratio           |
| `ans`      | `ans * 2` | Uses last ans | Last calculated result |

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

| Function | Example     | Result | Description       |
| -------- | ----------- | ------ | ----------------- |
| `sin(x)` | `sin(pi/2)` | 1      | Sine              |
| `cos(x)` | `cos(0)`    | 1      | Cosine            |
| `tan(x)` | `tan(pi/4)` | 1      | Tangent           |
| `csc(x)` | `csc(pi/2)` | 1      | Cosecant          |
| `sec(x)` | `sec(0)`    | 1      | Secant            |
| `cot(x)` | `cot(pi/4)` | 1      | Cotangent         |
| `rad(x)` | `rad(180)`  | 3.1415 | Degrees → Radians |
| `deg(x)` | `deg(pi)`   | 180    | Radians → Degrees |

---

## 🔄 **Inverse Trigonometric**

| Function      | Example       | Result | Description           |
| ------------- | ------------- | ------ | --------------------- |
| `asin(x)`     | `asin(0.5)`   | 0.523  | Inverse sine          |
| `acos(x)`     | `acos(0.5)`   | 1.047  | Inverse cosine        |
| `atan(x)`     | `atan(1)`     | 0.785  | Inverse tangent       |
| `acsc(x)`     | `acsc(2)`     | 0.523  | Inverse cosecant      |
| `asec(x)`     | `asec(2)`     | 1.047  | Inverse secant        |
| `acot(x)`     | `acot(1)`     | 0.785  | Inverse cotangent     |
| `atan2(y, x)` | `atan2(1, 1)` | 0.785  | 2-argument arctangent |

---

## 🌊 **Hyperbolic Functions**

| Function  | Example   | Result | Description          |
| --------- | --------- | ------ | -------------------- |
| `sinh(x)` | `sinh(0)` | 0      | Hyperbolic sine      |
| `cosh(x)` | `cosh(0)` | 1      | Hyperbolic cosine    |
| `tanh(x)` | `tanh(1)` | 0.761  | Hyperbolic tangent   |
| `csch(x)` | `csch(1)` | 0.850  | Hyperbolic cosecant  |
| `sech(x)` | `sech(1)` | 0.648  | Hyperbolic secant    |
| `coth(x)` | `coth(1)` | 1.313  | Hyperbolic cotangent |

---

## ♾️ **Inverse Hyperbolic**

| Function   | Example      | Result | Description                  |
| ---------- | ------------ | ------ | ---------------------------- |
| `asinh(x)` | `asinh(1)`   | 0.881  | Inverse hyperbolic sine      |
| `acosh(x)` | `acosh(2)`   | 1.316  | Inverse hyperbolic cosine    |
| `atanh(x)` | `atanh(0.5)` | 0.549  | Inverse hyperbolic tangent   |
| `acsch(x)` | `acsch(2)`   | 0.481  | Inverse hyperbolic cosecant  |
| `asech(x)` | `asech(0.5)` | 1.317  | Inverse hyperbolic secant    |
| `acoth(x)` | `acoth(2)`   | 0.549  | Inverse hyperbolic cotangent |

---

## 🎲 **Utility Functions**

| Function   | Example      | Result | Description         |
| ---------- | ------------ | ------ | ------------------- |
| `abs(x)`   | `abs(-10)`   | 10     | Absolute value      |
| `floor(x)` | `floor(3.9)` | 3      | Round down          |
| `ceil(x)`  | `ceil(3.1)`  | 4      | Round up            |
| `round(x)` | `round(3.6)` | 4      | Round to nearest    |
| `trunc(x)` | `trunc(3.9)` | 3      | Remove decimal part |
| `sign(x)`  | `sign(-8)`   | -1     | Sign of number      |
| `rand(x)`  | `rand(0)`    | 0–1    | Random number       |

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

| Function             | Example                    | Result | Description               |
| -------------------- | -------------------------- | ------ | ------------------------- |
| `memory_add(x)`      | `calc.memory_add(50)`      | —      | Add to memory (M+)        |
| `memory_subtract(x)` | `calc.memory_subtract(20)` | —      | Subtract from memory (M-) |
| `memory_recall()`    | `calc.memory_recall()`     | 50     | Recall stored value (MR)  |
| `memory_clear()`     | `calc.memory_clear()`      | —      | Clear memory (MC)         |
| `ans`                | `ans * 2`                  | —      | Last answer               |

---

## 🧩 **Special Behavior**

| Feature                 | Example         | Result | Description                      |
| ----------------------- | --------------- | ------ | -------------------------------- |
| Negative numbers        | `-5 + 3`        | -2     | Handles negative input correctly |
| Implicit multiplication | `2pi`           | 6.283  | Multiplies automatically         |
| Nested functions        | `sqrt(abs(-9))` | 3      | Supports layered expressions     |
| Domain validation       | `sqrt(-1)`      | Error  | Detects invalid math safely      |
