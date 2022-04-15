#importing the libraries
import random


#The list of programming languages to guess for the game.
guess_the_language_list = ['html','java', 'javascript', 'python', 'ruby', 'sql', 'php']


#Generates a random word to be guessed from the list of languages
language = random.choice(guess_the_language_list)
#Guessed word
language_guessed = list('*'*len(language))
#guessed letters
characters_guessed=[]


#This function reveals the '*' with each guessed character.
def reveal(guess):
    revealing_indices=[index for index,value in enumerate(language) if value==guess]
    global language_guessed
    for i in revealing_indices:
            language_guessed[i]=guess
    

#Welcome message printed to the screen.
print('Welcome to guess the programming language\n')
print('The programming language is: {}\n'.format(''.join(language_guessed)))


#Informing the user of how many failed attempts they have by using a print statement
print("You have a maximum of 5 failed attempts to guess the word")


#Getting the no.of failed attempts to find the word from the user.
chance = 0
while not int(chance) in range(1,6):
    try:
        chance = int(input("How difficult do you want to make the game?\nChoose the number of attempts you think you need to guess the hidden programming language [1-5]"))
    except:
        print('Enter between 1 and 5')
failed_attempts = 1




#Guessing begins
while failed_attempts<=chance:
    #prints the word and the guessed letters.
    print('\nGuess to reveal the programming language: ',''.join(language_guessed))
    print('Previous letters guessed: ', ','.join(characters_guessed))
    guess = input("Failed attempt number: {}\n".format(failed_attempts))



    #Executed when the letter has been already guessed.
    if guess in characters_guessed:
        print("You already tried that letter, please choose another letter that you have not chosen\n")
        continue
    characters_guessed.append(guess)


    
    #Executed when the user finds the entire word.
    if guess == language:
        print('You guessed the correct language\nThe programming language is: "{}"'.format(language))
        print("Congratulations!")
        exit(0)
        


    #Executed when the user guesses the letters in the word.
    if guess in language and len(guess)!=0:
        print('Correct, the letter "{}" is in this programming language'.format(guess))
        reveal(guess)
        
    else:
        print("Incorrect, please try again")
        failed_attempts+=1
    

    #Exits, When user finds the word.
    if '*' not in language_guessed:
        print('Congratulations, you have guessed the correct programming language, the language is: "{}"'.format(language))
        exit(0)
    

#Game over message printed to the screen with the correct word
print('Your loop has terminated:)\nThe programming language is: "{}"\nPlease revise your programming languages'.format(language))
exit(0)