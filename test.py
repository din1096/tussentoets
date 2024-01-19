import random
import time, math
sleutel = False
diamanten = 0
player_attack = 1
player_defense = 0
player_health = 3

def schatenkamer():
  print('Voorzichtig open je de deur, je wilt niet nog een monster tegenkomen.')
  print('Tot je verbazig zie je een schatkist in het midden van de kamer staan.')
  print('Je loopt er naartoe.')
  if sleutel == True:
    print('je pakt de sleutel en maakt de schatkist open')
    print('in de schatkist zit goud en diamanten')
    exit()
  else:
    print('je krijgt de schatkist niet open')
    exit()

def spinenkamer():
  spin_attack = 2
  spin_defense = 0
  spin_health = 3
  print('Dapper met je nieuwe item loop je de kamer binnen.')
  print('Je loopt tegen een spin aan.')

  spin_hit_damage = (spin_attack - player_defense)
  if spin_hit_damage <= 0:
    print('Jij hebt een te goede verdedigign voor de spin, hij kan je geen schade doen.')
  else:
    spin_attack_amount = math.ceil(player_health / spin_hit_damage)
    player_hit_damage = (player_attack - spin_defense)
    player_attack_amount = math.ceil(spin_health / player_hit_damage)

    if player_attack_amount < spin_attack_amount:
        print(f'In {player_attack_amount} rondes versla je de spin.')
        player_damage = player_attack_amount * spin_attack
        playerhealth = player_health - player_damage
        print(f'Je health is nu {playerhealth}.')
    else:
        print('Helaas is de spin te sterk voor je.')
        print('Game over.')
        exit()
  schatenkamer()

def wapenkamer():
  global player_attack
  global player_defense
  global diamanten
  print('je komt een nieuwe kamer binnen en ziet een goblin')
  print('hij zegt dat hij je iets kan verkopen als je een diamant hebt')
  print(f'je hebt {diamanten} diamanten')
  if diamanten == 1:
    print('hij zegt dat je een schild of een zwaard kan kopen')
    userInput = ""
    print('opties: zwaard/schild')
    userInput = input()
    if userInput == 'zwaard':
     print('je koos het zwaard')
     diamanten - 1
     player_attack += 2
    elif userInput  == 'schild':
     print('je koos het schild')
     diamanten - 1
     player_defense += 1
  elif diamanten >= 2:
    print('je kan een schild en het zwaard kopen')
    print('wil je ze allebij kopen')
    userInput = ''
    print('opties:ja/nee')
    userInput = input()
    if userInput == 'ja':
      print('je hebt het schild en het zwaard')
      diamanten - 2
      player_defense += 1
      player_attack += 2
  spinenkamer()




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
  global sleutel
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
    
  print('je ziet twee verschillende deuren')
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
  global diamanten
  diamanten += 1
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
  print('Door de twee grote deuren loop je een gang binnen.')
  print('Het ruikt hier muf en vochtig.')
  print('Je ziet een deur voor je.')
  diamantenkamer()

print("wat is je naam: ")
name = input()
print("veel geluk, " +name+ ".")
introscene()