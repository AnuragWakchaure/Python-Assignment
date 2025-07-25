
# Python Basics: Dictionary Lookup & List Slicing

This project contains two beginner-friendly Python tasks that demonstrate core concepts like using dictionaries, user input handling, list slicing, and reversing.

---

## ✅ Task 1: Create a Dictionary of Student Marks

### 📌 Problem Statement:
Write a Python program that:
1. Creates a dictionary with student names as keys and their marks as values.
2. Asks the user to input a student's name.
3. Retrieves and displays that student's marks.
4. If the student’s name is not found, displays an appropriate message.

### 📄 Example Code:
````markdown
```python
# Step 1: Create a dictionary of student marks
student_marks = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "David": 88,
    "Eva": 95
}

# Step 2: Ask for a student's name
name = input("Enter the student's name to retrieve their marks: ")

# Step 3: Display the result
if name in student_marks:
    print(f"{name}'s marks: {student_marks[name]}")
else:
    print(f"Student '{name}' not found in the record.")
````

### ✅ Sample Output:

```
Enter the student's name to retrieve their marks: Eva
Eva's marks: 95
```

### ❌ Output if name not found:

```
Enter the student's name to retrieve their marks: John
Student 'John' not found in the record.
```

---

## ✅ Task 2: Demonstrate List Slicing

### 📌 Problem Statement:

Write a Python program that:

1. Creates a list of numbers from 1 to 10.
2. Extracts the first five elements from the list.
3. Reverses those extracted elements.
4. Prints both the extracted and reversed lists.

### 📄 Example Code:

```python
# Step 1: Create a list from 1 to 10
numbers = list(range(1, 11))

# Step 2: Extract the first five elements
first_five = numbers[:5]

# Step 3: Reverse the extracted list
reversed_five = first_five[::-1]

# Step 4: Print the results
print("Original list:", numbers)
print("First five elements:", first_five)
print("Reversed first five elements:", reversed_five)
```

### ✅ Sample Output:

```
Original list: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
First five elements: [1, 2, 3, 4, 5]
Reversed first five elements: [5, 4, 3, 2, 1]
```

---

## 🛠 Requirements

* Python 3.x
* No external libraries needed

## 🏁 How to Run

1. Save each script as a `.py` file, such as `student_marks.py` and `list_slicing.py`.
2. Run them using a terminal or IDE:

   ```bash
   python student_marks.py
   python list_slicing.py
   ```

---

## 📚 Concepts Covered

* Dictionaries and key-value lookups
* Handling user input
* List slicing (`[:n]`)
* List reversing (`[::-1]`)
* Conditional statements

```


