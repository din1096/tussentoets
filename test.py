import random
import time, math
sleutel = False
loot = []
player_attack = 1
player_defense = 0
player_health = 3

def wapenkamer():
  global player_attack
  global player_defense
  print('je komt een nieuwe kamer binnen en ziet een goblin')
  print('hij zegt dat hij je iets kan verkopen als je een diamant hebt')
  print('hij zegt dat je een schild of een zwaard kan kopen')
  keuzes = ['zwaard','schilf']
  userInput = ""
  while userInput not in keuzes:
    print('opties: zwaard/schild')
    if userInput == 'zwaard':
     player_attack += 2
    elif userInput  == 'schild':
     player_defense += 2






def zombiekamer():
  zombie_attack = 1
  zombie_defense = 0
  zombie_health = 2
  print(f'je loopt een kamer binnen.')
  print('Je loopt tegen een zombie aan.')

  zombie_hit_damage = (zombie_attack - player_defense)
  if zombie_hit_damage <= 0:
    print('Jij hebt een te goede verdedigign voor de zombie, hij kan je geen schade doen.')
  else:
    zombie_attack_amount = math.ceil(player_health / zombie_hit_damage)
    
    player_hit_damage = (player_attack - zombie_defense)
    player_attack_amount = math.ceil(zombie_health / player_hit_damage)

    if player_attack_amount < zombie_attack_amount:
        print(f'In {player_attack_amount} rondes versla je de zombie.')
        player_damage = player_attack_amount * zombie_attack
        playerhealth = player_health - player_damage
        print(f'Je health is nu {playerhealth}.')
    else:
        print('Helaas is de zombie te sterk voor je.')
        print('Game over.')
        exit()
    wapenkamer()
    time.sleep(1)

def puzzelkamer():
  num1 = random.randint(10,25)
  num2 = random.randint(-5,75)
  print('Je stapt door de deur heen en je ziet een standbeeld voor je.')
  print('Het standbeeld heeft een sleutel vast.')
  print('Op zijn borst zit een numpad met de toesten 9 t/m 0.')
  print(f'Daarboven zie je een som staan {num1} + {num2} =?')
  antwoord = int(input('Wat toest je in?'))
  global sleutel
  som = num1 + num2
  if antwoord == som:
    sleutel = True
    print(f'Het stadbeeld laat de sleutel vallen en je pakt het op')
  elif antwoord != som:
    sleutel = False
    print('Er gebeurt niets....')
    
  print('je ziet twee verschillende kanten')
  print('welke kant wil je naartoe')
  kanten = ['links','boven']
  userInput = ""
  while userInput not in kanten:
     print("Options: links/boven")
     userInput = input()
     if userInput == 'links':
       zombiekamer()
     elif userInput == 'boven':
       wapenkamer()

  

def diamantenkamer():
  global loot
  loot.append('diamanten')
  print('je komt een kamer binnen met verschillende schaten')
  print('je ziet in het midden van de kamer een grote diamant je pakt het op')
  print('je ziet twee verschillende deuren')
  kanten = ['links','boven']
  userInput = ""
  while userInput not in kanten:
    print("Options: links/boven")
    userInput = input()
    if userInput == 'boven':
     wapenkamer()
    elif userInput == 'links':
     puzzelkamer()
    else:
      print('print en valid option')



def introscene():
  kanten = ['links']
  print('Door de twee grote deuren loop je een gang binnen.')
  print('Het ruikt hier muf en vochtig.')
  print('Je ziet een deur voor je.')
  print('wil je naar de volgende kamer')
  userInput = ""
  while userInput not in kanten:
    print("Options: ja/nee")
    userInput = input()
    if userInput == "ja":
      diamantenkamer()
    else:
      print('dat kan niet')
  



if __name__ == "__main__":
  while True:
    print("je begint een dungeon te exploren op zoek naar schaten.")
    print("je moet puzzels en monsters verslaan om te winne")
    print("wat is je naam: ")
    name = input()
    print("veel geluk, " +name+ ".")
    introscene()