# list1.py

mylist = []

def append1(x):
    mylist.append(x)
    print("Appended:", x)

def extend1(l):
    mylist.extend(l)
    print("Extended with:", l)

def pop():
    if mylist:
        print("Popped:", mylist.pop())
    else:
        print("List is empty")

def remove1(x):
    if x in my_list:
        mylist.remove(x)
        print("Removed:", x)
    else:
        print("Value not found in list")
