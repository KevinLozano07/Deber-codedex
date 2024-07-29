# Write code below 💖

print("")
height = int(input("¿Cuál es tu altura en cm? "))
print("")
credits = int(input("¿Cuántos créditos tienes? "))
print("")

if height >= 137 and credits >= 10:
    print("")
    print("Enjoy the ride!")
    print("")
elif credits >= 10 and height < 137:
    print("")
    print("You are not tall enough to ride.")
    print("")
elif height >= 137 and credits < 10:
    print("")
    print("You don't have enough credits.")
    print("")
else:
    print("")
    print("You have not met either requirement.")
    print("")