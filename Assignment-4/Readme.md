



````markdown
# Python File Handling Tasks

This project contains two basic Python programs that demonstrate reading from and writing to files, along with proper error handling and user interaction.

---

## ✅ Task 1: Read a File and Handle Errors (With Line Numbers)

### 📌 Problem Statement:
Write a Python program that:
1. Opens and reads a file named `sample.txt`.
2. Prints the content line by line with line numbers (e.g., `Line 1: ...`).
3. Gracefully handles the error if the file does not exist.

### 📄 Example Code:
```python
try:
    file = open("sample.txt", "r")

    print("File content:\n")
    line_number = 1
    line = file.readline()

    while line:
        print(f"Line {line_number}: {line.strip()}")
        line_number += 1
        line = file.readline()

    file.close()
except FileNotFoundError:
    print("Error: The file 'sample.txt' does not exist.")
````

### ✅ Sample Output (when file exists):

```
File content:

Line 1: Hello, this is a sample file.
Line 2: It contains a few lines of text.
Line 3: Enjoy reading!
```

### ❌ Sample Output (when file does not exist):

```
Error: The file 'sample.txt' does not exist.
```

---

## ✅ Task 2: Write and Append Data to a File

### 📌 Problem Statement:

Write a Python program that:

1. Takes user input and writes it to `output.txt`.
2. Appends more user input to the same file.
3. Reads and displays the final contents of the file with line numbers.

### 📄 Example Code:

```python


user_input = input("Enter text to write to the file: ")

with open("output.txt", "w") as file:
    file.write(user_input + "\n")
print("Data successfully written to output.txt")


additional_input = input("Enter additional text to append: ")

with open("output.txt", "a") as file:
    file.write(additional_input + "\n")
print("Data successfully appended")


print("\nFinal content of output.txt:\n")

with open("output.txt", "r") as file:
    for line in file:
        print( line.strip())


        
```

### ✅ Sample Run:

```
Enter some data to write to the file: 25
Enter additional data to append to the file: This is appended data.

Final content of output.txt:

Line 1: 25
Line 2: This is appended data.
```

---

## 🛠 Requirements

* Python 3.x
* No external libraries required

## 🏁 How to Run

1. Save each task in its own `.py` file (e.g., `read_file.py`, `write_append_file.py`)
2. Run the files using:

   ```bash
   python read_file.py
   python write_append_file.py
   ```

---

## 📚 Concepts Covered

* File reading and writing
* While loops
* Error handling using `try-except`
* User input handling
* String manipulation with `.strip()`

```

