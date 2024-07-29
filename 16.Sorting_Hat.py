# Write code below 💖

Gryffindor = 0
Ravenclaw = 0
Hufflepuff = 0
Slytherin = 0

print("")
print("Do you like Dawn or Dusk?")
print("1) Dawn")
print("2) Dusk")
print("")
Q1 = input("Answer: ")

if Q1 == "1" or Q1 == "Dawn":
    Gryffindor = Gryffindor + 1
    Ravenclaw = Ravenclaw + 1
elif Q1 == "2" or Q1 == "Dusk":
    Hufflepuff = Hufflepuff + 1
    Slytherin = Slytherin + 1
else:
    print("Wrong input.")

print("")
print("When I’m dead, I want people to remember me as:")
print("1) The Good")
print("2) The Great")
print("3) The Wise")
print("4) The Bold")
print("")
Q2 = input("Answer: ")

if Q2 == "1" or Q2 == "The Good":
    Hufflepuff = Hufflepuff + 2
elif Q2 == "2" or Q2 == "The Great":
    Slytherin = Slytherin + 2
elif Q2 == "3" or Q2 == "The Wise":
    Ravenclaw = Ravenclaw + 2
elif Q2 == "4" or Q2 == "The Bold":
    Gryffindor = Gryffindor + 2
else:
    print("Wrong input.")

print("")
print("Which kind of instrument most pleases your ear?")
print("1) The violin")
print("2) The trumpet")
print("3) The piano")
print("4) The drum")
print("")
Q3 = input("Answer: ")

if Q3 == "1" or Q3 == "The violin":
    Slytherin = Slytherin + 4
elif Q3 == "2" or Q3 == "The trumpet":
    Hufflepuff = Hufflepuff + 4
elif Q3 == "3" or Q3 == "The piano":
    Ravenclaw = Ravenclaw + 4
elif Q3 == "4" or Q3 == "The drum":
    Gryffindor = Gryffindor + 4
else:
    print("Wrong input.")

if Gryffindor > Slytherin and Gryffindor > Hufflepuff and Gryffindor > Ravenclaw:
    print("")
    print("Your house will be: 🦁 Gryffindor")
    print("")
elif Slytherin > Gryffindor and Slytherin > Hufflepuff and Slytherin > Ravenclaw:
    print("")
    print("Your house will be: 🐍 Slytherin")
    print("")
elif Hufflepuff > Slytherin and Hufflepuff > Gryffindor and Hufflepuff > Ravenclaw:
    print("")
    print("Your house will be: 🦡 Hufflepuff")
    print("")
else:
    print("")
    print("Your house will be: 🦅 Ravenclaw")
    print("")