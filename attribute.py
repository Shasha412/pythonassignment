# Make attribute errors handler with built in exceptions. 

a = 'Python'
obj = "class"
try:
    print(obj.a)
    print(obj.b)
except AttributeError:
    print("Error in attribute")
