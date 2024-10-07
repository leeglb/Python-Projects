import random as random

#while the function is true, (boolean is always true) the function will constantly ask and choose random variables 

while True: 
    for i in ['1','2','3','4','5','6','7','8','9','10']:
        value = i 

    random_value = random.choice(value)

    count = 0 

    user_input = str(input("Enter any number between 1 and 10: "))
    if user_input == random_value:
        count += 1
        print("You Guessed It!\n" + "Win Count:" + f"{count}")
    else:
        print("Incorrect!")