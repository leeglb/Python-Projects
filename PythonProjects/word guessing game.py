import random as random

count = 0
word_count = 5

while count < 5:

    first_print = "\nEnter" +" " + f"{word_count}" + " " + "words"
    print(first_print)

    user_input = str(input("\nEnter your first words: "))
    word_list = []
    word_list.append(user_input)
    count += 1
    word_count -= 1 

if count == 5:
    second_input = str(input("\nEnter your guess: "))
    guess = random.choice(first_print)
    if second_input == guess:
        print("You Got It!")
    while second_input != guess:
        print("\nTry again!")
        second_input = str(input("\nEnter your guess: "))

    