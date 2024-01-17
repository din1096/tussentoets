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
}
 
current_kamer = 'startkamer'

print(kamers[current_kamer]['description'])