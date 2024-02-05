myList = [1,3.6,"Four"]

myTuple = (1,3.6,"Four")

#tuples are immutable.  can't add, change or remove elements
myTest = tuple(myList)

#lists are mutable
myTest = list(myTest)

#the benefits of tuples are efficiency and performance

print(myTuple[0])
print(myTuple[-1])
print(myTuple[1:3])
print(myTuple.index(3.6))
3.6 in myTuple