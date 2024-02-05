"""
    loops
    
    while some condition is true:
        do something
        test if the condition is still true
"""

i = 1
while i <= 5:
    print(i)
    i+=1
    
i = 1
while i <= 5:
    if i == 3:
        break
    print(i)
    i+=1
    
    