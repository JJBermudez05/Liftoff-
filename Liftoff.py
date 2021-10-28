# Compares the palyer's guess tot the secret to the secret code by looking at each digit, one at a time. 

def compare_guess(secret_code, guess) :
    
    num_spaceships = 0

    num_aliens = 0

    for i in range (4) :

        if guess [i] == secret_code [i] :

            num_spaceships += 1

        elif guess [i] in secret_code:

            num_aliens += 1

            result = f"{num_spaceships}S{num_aliens}A"

            return result

print("Welcome to Spaceships and Aliens!")

print("Your goal is to crack a secret 4-digit code. All the digits in the code are unique!")

print("A spaceship(S) means you've guessed the right digit at the right position.")

print("An alien (A) means you've guess the right digit, but at the wrong position!")

print("Wrong digits get ignored.")

secret_code = input("Pick a secret code with 4 different digits: ")

for counter in range(100) :
    
    print()

guess = "0000"

while secret_code != guess:
    
    guess = input("Enter a 4 digit code: ")

    result = compare_guess(secret_code, guess)

    if result == "4S0A" :

        print("Congratulations! You broke the secret code!")

    else: 

        print(result)


