# set2.py

myset = set()

def slen2(s):
    print("Length of set:", len(s))

def adds2(x):
    myset.add(x)
    print("Added to set:", x)

def remove2(x):
    if x in myset:
        myset.remove(x)
        print("Removed from set:", x)
    else:
        print("Element not found in set")
