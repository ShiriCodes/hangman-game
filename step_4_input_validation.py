word = input("Please enter a word: ") #asking for a word input
print("_ "*len(word)) #mirroring number of letters in said word
guess = input("Guess a letter:") #asking for a guess input
if len(guess)==1 and guess.isalpha(): #validating that the guess is in fact 1 letter long and does not contain special symbols
    print(guess.lower()) #mirroring validated guess
elif len(guess)>1 and guess.isalpha(): #checking if guess is too long but does not contain any special symbols
    print("E1") #Error message no. 1
elif len(guess)==1 and not guess.isalpha(): #checking if guess is not too long but does contain special symbols
    print("E2") #Error message no. 2
else: ##checking if guess is both too long and does contain any special symbols
    print("E3") #Error message no. 3
