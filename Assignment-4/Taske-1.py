try:
    file = open("file.txt", "r")

    print("Reading file content:\n")
    line_number = 1
    line = file.readline()

    while line:
        print(f"Line {line_number}: {line.strip()}")
        line_number += 1
        line = file.readline()

    file.close()
except FileNotFoundError:
    print("Error: The file 'file.txt' does not exist.")
