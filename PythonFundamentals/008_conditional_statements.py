"""
   If it's sunny today, 
       I'll go for a run
"""

weather = "sunny"

if weather == "sunny":
    print("I'll go for a run.")
    
    
    weather = "cloudy"

    if weather == "sunny":
        print("I'll go for a run.")
    elif weather == "cloudy":
        print("let's go to the gym.")
    else:
        print("let's just stay in.")
        
        
        
        weather = "sunny"
        temp = 20

        if weather == "sunny" and temp > 15:
            print("I'll go for a run.")              
        else:
            print("let's just stay in.")
            
            weather = "sunny"
            temp = 12

            if weather == "sunny" or temp > 15:
                print("I'll go for a run.")              
            else:
                print("let's just stay in.")
                

i = 3
if i % 2 == 0 :
    print(f"{i} is an even number")
else:
    print(f"{i} is a bit odd")
        