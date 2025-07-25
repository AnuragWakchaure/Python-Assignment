```markdown
# Python Basics: Factorial Function & Math Module Calculations

This repository contains two simple Python tasks demonstrating fundamental programming concepts using functions and built-in modules.

---

## Task 1: Calculate Factorial Using a Function

### ✅ Problem Statement:
Write a Python program that:
- Defines a function named `factorial` which takes a number as input.
- Calculates the factorial using a loop.
- Returns the calculated factorial.
- Calls the function with a sample number and prints the result.

### 📌 Sample Output:
If the input is `5`, the output will be:
```

The factorial of 5 is: 120

````

### 📄 Example Code:
```python
def factorial(n):
    if n < 0:
        return "Factorial does not exist for negative numbers"
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

# Sample call
number = 5
print(f"The factorial of {number} is: {factorial(number)}")
````

---

## Task 2: Using the Math Module for Calculations

### ✅ Problem Statement:

Write a Python program that:

* Takes a number as input from the user.
* Uses the `math` module to calculate:

  * Square root
  * Natural logarithm (ln)
  * Sine (in radians)
* Displays the calculated results.

### 📌 Sample Output:

If the user inputs `25`, the output will be:

```
Enter a number: 25

Results for number 25.0:
Square root: 5.0
Natural logarithm (ln): 3.2188758248682006
Sine (in radians): -0.13235175009777303
```

### 📄 Example Code:

```python
import math

# Ask the user for a number
num = float(input("Enter a number: "))

# Perform calculations using the math module
sqrt_val = math.sqrt(num)
log_val = math.log(num)
sine_val = math.sin(num)

# Display the results
print(f"\nResults for number {num}:")
print(f"Square root: {sqrt_val}")
print(f"Natural logarithm (ln): {log_val}")
print(f"Sine (in radians): {sine_val}")
```

---

## 🛠 Requirements

* Python 3.x
* No additional libraries required (only built-in `math` module)

## 🏁 How to Run

1. Save the scripts as separate `.py` files (e.g., `factorial.py` and `math_calculations.py`)
2. Run them using:

   ```bash
   python factorial.py
   python math_calculations.py
   ```

---

## 📚 Topics Covered

* Python functions
* Loops
* User input
* Math module usage
* Basic mathematical operations


