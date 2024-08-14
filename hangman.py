import random as random

word_choice = []

word_counter = 5


while word_counter > 0:

    word_choice_input = str(input("\nEnter" + " " + f"{word_counter}" + " " + "words: "))

    word_counter -= 1 

    word_choice.append(word_choice_input)

if word_counter == 0:

    tick = 0 

    random_word = random.choice(word_choice)

    random_length = len(random_word)

    for i in range(len(random_word)): #for i in range the word 

        print(i * "_", end="")

    x_attempt = str(input("\nEnter your first guess: "))

    for char in random_word: #each character in word

        if x_attempt == char: #if the str is equal to the character

            pass
                        

                
        
            
            
