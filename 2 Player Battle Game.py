import os, time, random

def rollDice(sides):
  dice_sides = random.randint(0, sides)
  return dice_sides

def health():
  six_sided_roll = rollDice(6)
  twelve_sided_roll = rollDice(12)
  health = int(six_sided_roll*twelve_sided_roll / 2 + 10)
  return health

def strength():
  six_sided_roll = rollDice(6)
  twelve_sided_roll = rollDice(12)
  strength = int(six_sided_roll*twelve_sided_roll /2 + 12)
  return strength



os.system("cls") #clears all after first character creation
print("Welcome, dear warriors!")
time.sleep(1)
print("You came here today to dare.")
time.sleep(1)
print("To hope.")
time.sleep(1)
print("To fight!")
print()
time.sleep(3)
os.system("cls") #clears the intro
#starts the character creator
print("⚔️  Create your characters! ⚔️")
print()
time.sleep(1)
#player 1 character creation
player1_name = input("Your character name: ").upper() #name1
player1_type = input("Character Type (Human, Elf, Mage, Orc, Banshee): ").upper() #type1
print()
print(player1_name + " " + "THE" + " " + player1_type + " " + "📜")
player1_health = health() #health1
player1_strength = strength() #strength1
time.sleep(1)
print("HEALTH:",player1_health, "❤️")
time.sleep(1)
print("STRENGTH:",player1_strength, "🔥")
print()
print()
time.sleep(1)
print("Who are they battling?")
print()
print()
time.sleep(1)
#player 2 character creation
player2_name = input("Your character name: ").upper() #name2
player2_type = input("Character Type (Human, Elf, Mage, Orc, Banshee): ").upper() #type2
print()
print(player2_name + " " + "THE" + " " + player2_type + " " + "📜")
player2_health = health() #health2
player2_strength = strength() #strength2
time.sleep(1)
print("HEALTH:",player2_health, "❤️")
time.sleep(1)
print("STRENGTH:",player2_strength, "🔥")
time.sleep(4)
os.system("cls")

round = 1
winner = None

#battle time
while True:
  time.sleep(3)
  os.system("cls")
  print("⚔️ BATTLE TIME ⚔️")
  print()
  print(f'Let the battle begin! Round: {round}')
  print()

  player1_roll = rollDice(6)
  player2_roll = rollDice(6)

  damage = abs(player1_strength - player2_strength) + 1

  if player1_roll > player2_roll:
    player2_health -= damage
    if round == 1:
      time.sleep(2)
      print(f'{player1_name} took the first blow!\n{player2_name} takes {damage} damage')
    else:
      time.sleep(2)
      print(f'{player1_name} wins round: {round}')
    
  elif player1_roll < player2_roll:
    player1_health -= damage
    if round == 1:
      time.sleep(2)
      print(f'{player2_name} took the first blow!\n{player1_name} takes {damage} damage')
    else:
      time.sleep(2)
      print(f'{player2_name} wins round {round}')

  else:
    print(f'Their swords clash and they draw the round {round}')

  print()
  time.sleep(1)
  print(player1_name)
  print("REMAINING HEALTH: ", player1_health)
  print()
  time.sleep(1)
  print(player2_name)
  print("REMAINING HEALTH: ", player2_health)
  print()

  
  if player1_health <= 0:
    print(f'{player1_name} has died!')
    winner = player2_name
    break
  elif player2_health <= 0:
    print(f'{player2_name} has died!')
    winner = player1_name
    break
  else:
    time.sleep(1)
    print("And the're both standing for the next round!")
    round += 1

time.sleep(2)
os.system("cls")
print("⚔️  BATTLE TIME ⚔️")
print()
print(f'{winner} has won in {round} rounds!')
print()

