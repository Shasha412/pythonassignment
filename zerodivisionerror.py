# Make a zero division error handler with built in exceptions

numerator = int(input("Enter the numerator"))
try:
    result = numerator / 0
except ZeroDivisionError :
    print("Error: Cannot divide by zero.")
except ValueError :
    print("error in value")
print(numerator)
