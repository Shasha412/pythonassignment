# Make file not found error handler with built in exceptions. 

try:
    with open("nonexistent_file.txt", "r") as file:
        content = file.read()
    print(content)
except FileNotFoundError:
    print("Error: The file was not found.")
