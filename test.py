import random
import time, math
player_attack = 1
player_defense = 0
player_health = 3
kamers = {
    "startkamer":{
        "description": 'Door de twee grote deuren loop je een gang binnen Het ruikt hier muf en vochtig.je ziet een deur voor je',
        'exits':{'links':'kamer2'}
    },
    "kamer2":{
        "description":'Je stapt door de deur heen en je ziet een standbeeld voor je.Het standbeeld heeft een sleutel vast '
        'Op zijn borst zit een numpad met de toesten 9 t/m 0.. ',
        'exits':{'links':'kamer6','boven':'kamer3'}
    },
    "kamer3":{
        "description":"Je duwt hem open en stap een hele lange kamer binnen.",
     'exits':{'boven':'kamer4'}
    },
    'kamer4':{
        'description':"je loopt de kamer binnen en je ziet een spin hij rent naar je toe",
        'exits':{"links":"kamer5"}
    },
    "kamer5":{
        'description':"Voorzichtig open je de deur, je wilt niet nog een monster tegenkomen.Tot je verbazig zie je een schatkist in het midden van de kamer staan",
    },
    "kamer6":{
        'description':"je loopt een kamer binnen Je ziet een zombie aan hij rent naar je toe",
        'exits':{'rechts':'kamer3'}
    },
}
 
current_kamer = 'startkamer'
while True:
    print(kamers[current_kamer]['description'])
    richting = input('welke kant wil je op?')
    if richting in ['links','rechts','boven','beneden']:
        if richting in kamers[current_kamer]['exits']:
            current_kamer = kamers[current_kamer]['exits'][richting]
        else:
            print('je kan de kant niet op')
    else:
        print('dat ken ik niet')