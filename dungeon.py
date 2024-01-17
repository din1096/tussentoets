import random
import time, math
player_attack = 1
player_defense = 0
player_health = 3

# === [kamer 1] === #
print('Door de twee grote deuren loop je een gang binnen.')
print('Het ruikt hier muf en vochtig.')
print('Je ziet een deur voor je.')
print('')
time.sleep(1)

# === [kamer 2] === #
num1 = random.randint(10,25)
num2 = random.randint(-5,75)
print('Je stapt door de deur heen en je ziet een standbeeld voor je.')
print('Het standbeeld heeft een sleutel vast.')
print('Op zijn borst zit een numpad met de toesten 9 t/m 0.')
print(f'Daarboven zie je een som staan {num1} + {num2} =?')
antwoord = int(input('Wat toest je in?'))
som = num1 + num2
if antwoord == som:
    sleutel = True
    print(f'Het stadbeeld laat de sleutel vallen en je pakt het op')
elif antwoord != som:
    sleutel = False
    print('Er gebeurt niets....')

print('Je ziet twee deuren achter het standbeeld.')

print('je loopt naar de deur toe en maakt hem open')
time.sleep(1)

# === [kamer 6] === #
zombie_attack = 1
zombie_defense = 0
zombie_health = 2
print('je loopt een kamer binnen.')
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
        new_playerhealth = int(player_attack_amount * zombie_attack)
        print(f'Je health is nu {new_playerhealth}.')
    else:
        print('Helaas is de zombie te sterk voor je.')
        print('Game over.')
        exit()
print('')
time.sleep(1)

# === [kamer 3] === #
item = ['schild','zwaart']
num3 = random.randint(1,10)
if num3 >= 5:
    item.remove('zwaart')
    player_defense += 1
    print('Je duwt hem open en stap een hele lange kamer binnen.')
    print(f'In deze kamer staat een tafel met daarop een {item}.')
    print(f'Je pakt het {item} op en houd het bij je.')
    print('Op naar de volgende deur.')
    print('')
    time.sleep(1)
else:
    item.remove('schild')
    player_attack += 2
    print('Je duwt hem open en stap een hele lange kamer binnen.')
    print(f'In deze kamer staat een tafel met daarop een {item}.')
    print(f'Je pakt het {item} op en houd het bij je.')
    print('Op naar de volgende deur.')
    print('')
    time.sleep(1)

# === [kamer 4] === #
spin_attack = 2
spin_defense = 0
spin_health = 3
print(f'Dapper met je nieuwe {item} loop je de kamer binnen.')
print('Je ziet daar een grote spin.')

spin_hit_damage = (spin_attack - player_defense)
if spin_hit_damage <= 0:
    print('Jij hebt een te goede verdedigign voor de spin, hij kan je geen schade doen.')
else:
    spin_attack_amount = math.ceil(player_health / spin_hit_damage)
    
    player_hit_damage = (player_attack - spin_defense)
    player_attack_amount = math.ceil(spin_attack / player_hit_damage)

    if player_attack_amount < spin_attack_amount:
        print(f'In {player_attack_amount} rondes versla je de spin.')
        new_playerhealth = int(player_attack_amount * spin_attack)
        print(f'Je health is nu {new_playerhealth}.')
    else:
        print('Helaas is de spin te sterk voor je.')
        print('Game over.')
        exit()
print('')
time.sleep(1)

# === [kamer 5] === #

print('Voorzichtig open je de deur, je wilt niet nog een zombie tegenkomen.')
print(f'Tot je verbazig zie je een schatkist in het midden van de kamer staan.')
print('Je loopt er naartoe.')
if sleutel == True:
    print('je pakt de sleutel en maakt de schatkist open')
    print('in de schatkist zit goud en diamanten')
    exit()
else:
    print('je krijgt de schatkist niet open')
    exit()