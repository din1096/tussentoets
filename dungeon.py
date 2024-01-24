import random
import time, math
sleutel = False
rubies = 0
player_attack = 1
player_defense = 0
player_health = 3

def toverkamer():
  global player_health
  global player_defense
  print('je komt in een kamer en hoort een stem')
  print('hij zegt dat je mag kiesen tussen meer health of meer defence')
  print('wat wil je opties: defence health')
  input('')
  if input == 'defence':
    player_defense += 1
    wapenkamer()
  elif input == 'health':
    player_health += 2
    wapenkamer()
  
  
  
  

def gokkamer():
  global rubies
  global player_health
  num1 = random.randint(1,6)
  num2 = random.randint(1,6)
  som = num1 + num2
  print('je loopt een kamer in en ziet een grote gokmachine')
  print('je kan hem gebruiken om je rubies te verdubelen')
  print('wil je hem gebruiken opties: ja/nee')
  antwoord = input('')
  if antwoord == 'ja':
    if som > 7:
      rubies * 2
      print(f'je rubies zijn verdubbelt je hebt {rubies} rubies')
      toverkamer()
    elif som < 7:
      print('je verloor je verliest 1 health')
      player_health - 1
      toverkamer()
    elif som == 7:
      print('je rubies zijn verduppelt en je verliest 1 health')
      rubies * 2
      player_health - 1
      toverkamer()
  elif antwoord == 'nee':
    toverkamer()
  
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
  global rubies
  print('je komt een nieuwe kamer binnen en ziet een goblin')
  print('hij zegt dat hij je iets kan verkopen als je een rubies hebt')
  print(f'je hebt {rubies} rubies')
  if rubies == 1:
    print('hij zegt dat je een schild of een zwaard kan kopen')
    userInput = ""
    print('opties: zwaard/schild')
    userInput = input()
    if userInput == 'zwaard':
     print('je koos het zwaard')
     rubies - 1
     player_attack += 2
    elif userInput  == 'schild':
     print('je koos het schild')
     rubies - 1
     player_defense += 1
  elif rubies >= 2:
    print('je kan een schild en het zwaard kopen')
    print('wil je ze allebij kopen')
    userInput = ''
    print('opties:ja/nee')
    userInput = input()
    if userInput == 'ja':
      print('je hebt het schild en het zwaard')
      rubies - 2
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
    gokkamer()
    time.sleep(1)

def puzzelkamer():
  num1 = random.randint(10,25)
  num2 = random.randint(-5,75)
  global rubies
  print('Je stapt door de deur heen en je ziet een standbeeld voor je.')
  print('Het standbeeld heeft een ruby vast.')
  print('Op zijn borst zit een numpad met de toesten 9 t/m 0.')
  print(f'Daarboven zie je een som staan {num1} + {num2} =?')
  antwoord = int(input('Wat toest je in?'))
  som = num1 + num2
  if antwoord == som:
    print(f'Het stadbeeld laat de ruby vallen en je pakt het op')
    rubies += 1
  elif antwoord != som:
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
       gokkamer()

def diamantenkamer():
  num1 = random.randint(1,10)
  global rubies
  print('je komt een kamer binnen met verschillende schaten')
  if num1 < 10:
    rubies += 1
    print('je ziet in het midden van de kamer een grote ruby je pakt het op')
    print('je ziet twee verschillende deuren')
    kanten = ['links','boven']
    userInput = ""
    while userInput not in kanten:
     print("Options: links/boven")
     userInput = input()
     if userInput == 'boven':
      gokkamer()
     elif userInput == 'links':
      puzzelkamer()
     else:
       print('print en valid option')
  else:
    print('er zit niks in de schatkisten')
    print('je ziet twee verschillende deuren')
    kanten = ['links','boven']
    userInput = ""
    while userInput not in kanten:
     print("Options: links/boven")
     userInput = input()
     if userInput == 'boven':
      gokkamer()
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