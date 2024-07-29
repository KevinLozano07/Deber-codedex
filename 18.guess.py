# Write code below 💖

guess = 0
tries = 0

while guess != 6 and tries < 5:
    print("")
    guess = int(input('Guess the number:  '))
    tries = tries + 1 

if guess == 6:
    print("")
    print("You got it!")
    print("")
else:
    print("")
    print("Maximum number of attempts reached")
    print("")