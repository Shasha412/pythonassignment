# Make module not found error handler with built in exceptions. 

try:
    import non_existing_module
except ModuleNotFoundError:
    print("Error: no such module exist")
