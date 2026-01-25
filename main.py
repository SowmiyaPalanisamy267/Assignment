import random

secret_number = random.randint(1, 100)

guess = int(input("Enter any number between 1 and 100: "))
while secret_number!= guess:

    if guess < secret_number:
        print("Too low")
        guess = int(input("Enter number again: "))
    elif guess > secret_number:
        print("Too high!")
        guess = int(input("Enter number again: "))
    else:
        break
print("you guessed it right!!")



import random
words = ['python', 'javascript', 'java', 'automation', 'pytest', 'guvi', 'selenium']
original_word = random.choice(words)
scrambled_word = ''.join(random.sample(original_word, len(original_word)))
print("your scrambled word is:", scrambled_word)

while True:
        guess = input("Enter Your guess: ").lower()

        if guess == original_word:
            print("Correct! Well done!")
            break
        else:
            print("Wrong guess, try again.")
