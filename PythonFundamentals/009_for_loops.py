"""
    loops
    
    for each element in a collection
      do something
"""

my_string = "a cup of coffee"

for i in my_string:
    print(i)

for i in my_string:
    print(i.upper())


# loops rely on indentation to scope the code block
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in my_list:
    i_squared = i ** 2
    print(i, i_squared)

my_list = ["a", "b", "c"]
for i, j in enumerate(my_list):
    print(i, j)

# nesting loops
for i in my_list:
    for j in my_list:
        print(i, j)

#range (start, stop, step)

my_nums = list(range(0, 20))
print(my_nums)

for i in my_nums:
    if i % 2 == 0:
        print(f"{i} is even stevens.")
    else:
        print(f"{i} is a bit odd.")


for i in range(0, 21):
    if i % 3 == 0:
        # continue skips to the next element in the loop
        continue
    print(i)

for i in range(0, 21):
    if i % 3 == 0:
        # pass = do nothing
        pass
    print(i)

for i in range(1, 21):
    if i % 3 == 0:
        break
    print(i)
