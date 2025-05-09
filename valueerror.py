# Make value errors handler with built in exceptions. 

try:
    x = int("str")  
    i = 1 / x
except ValueError:
    print("Error in value")
except ZeroDivisionError:
    print("Error in Division")
