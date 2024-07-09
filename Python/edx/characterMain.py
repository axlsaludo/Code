
# Test Bench for Character Class

from character import Character
from character import Enemy

dave = Enemy("Dave", "A smelly zombie")
dave.setWeakness("cheese")


print ("what will you fight with?")
fight_with = input()
dave.fight(fight_with)