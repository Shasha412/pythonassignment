# Make a key error handler with built in exceptions.

d = {"apple": 1, "banana": 2, "cherry": 3}
try:
    value = d["grape"]
except KeyError:
    print("Error in key")
except ValueError :
    print("error in value")
