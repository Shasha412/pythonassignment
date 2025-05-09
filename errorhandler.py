# Make an error handler with the use of multiple except for all types of errors. 

d = [3,5,7,2,6]
x = {"apple": 1, "banana": 2, "cherry": 3}
try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = num1 / num2
    print("Result:", result)
    print(d[12])
    value = x["grape"]
except IndexError:
    print("Error in index")
except ValueError:
    print("Error in value")
except ZeroDivisionError:
    print("Error in division")
except NameError :
    print("Error in name")
except KeyError:
    print("Error in key")
except Exception as e:
    print("Error in code")
