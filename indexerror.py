# Make index error handler with built in exceptions. 

d = [3,5,7,2,6]
try:
    print(d[12])
except IndexError:
    print("Error in index")
except ValueError :
    print("error in value")
