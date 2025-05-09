# dict3.py

mydict = {}

def len3(d):
    print("Dictionary length:", len(d))

def add3(k, v):
    mydict[k] = v
    print(f"Added ({k}: {v})")

def keys3():
    print("Keys:", list(mydict.keys()))

def values3():
    print("Values:", list(mydict.values()))
