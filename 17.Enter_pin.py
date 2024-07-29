# Write code below 💖

print("")
print('BANK OF CODÉDEX')

print("")
pin = int(input('Enter your PIN: '))

while pin != 1234:
  print("")
  pin = int(input('Incorrect PIN. Enter your PIN again: '))
  
if pin == 1234:
  print("")
  print('PIN accepted!')
  print("")