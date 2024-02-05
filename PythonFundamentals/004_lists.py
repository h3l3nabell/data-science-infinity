list1 = []
list2 = list()
type(list1)
type(list2)

list3 = [1, 2.55, "three", 400000, True]
print(list3)
len(list3)

print(list3[0])
print(list3[3])

# print(list3[5])

print(list3[-1])
print(list3[-2])

# list3[start:end]
list3[2:4]
list3[:4]
list3[2:]

planetList = ["Mercury", "Venus", "Earth"]

planetList.append("Jupiter")
planetList.insert(3, "Mars")

outerPlanetList = ["Saturn", "Uranus", "Neptune", "Pluto"]
planetList.extend(outerPlanetList)

[1, 2, 3] + [4, 5, 6]

# removing elements
planetList.remove("Pluto")
print(planetList)

del planetList[2]

planetList.pop(2)

# finding elements

planetList.index("Mercury")
planetList.index("Tatooine")

"Earth" in planetList
"Tatooine" in planetList

planetList.sort()
planetList.sort(reverse=True)

# copying lists
list1 = [1, 2, 3]
list2 = list1.copy()
list2.append(4)
