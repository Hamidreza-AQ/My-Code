import pandas as pd 
import random 
diself = {"water":["fire","earth"],
        "fire":["nature"],
        "nature":["water","earth"],
        "electric":["water"],
        "earth":["electric","fire"]}

class Creature():
    def __init__(self,name,strength,speed,defense,health,max_health,element):
        self.name = name
        self.strength = strength
        self.speed = speed
        self.defense = defense
        self.health = health
        self.max_health = max_health
        self.element = element
        self.alive = True

    def status(self):
        return f"""
name : {self.name} 
strength : {self.strength} 
speed : {self.speed} 
defense : {self.defense} 
health : {self.health} 
element : {self.element} 
alive : {self.alive}"""

    def take_damage(self,amount):
        self.health -= amount
        if self.health <= 0:
            self.alive = False

    def is_alive(self):
        return self.alive

    def attack(self,target):
        damage = self.strength - (target.defense // 2)

        if target.element in diself[self.element]:
            damage += 50
        elif self.element in diself[target.element]:
            damage -= 25

        num = random.randint(0,20)
        damage += num
        damage = max(0,damage)
        target.take_damage(damage)

        return f"{self.name} be {target.name} {damage} ta asib zad!"
    
    def fight(self,other):
        turns = 0
        if self.speed > other.speed:
            attacker , defender = self , other 
        elif other.speed > self.speed:
            attacker , defender = other , self
        else:
            attacker , defender = random.choice([(self,other),(other,self)])
        while True:
            print(attacker.attack(defender))
            turns += 1
            if defender.is_alive() == False:
                winner = attacker
                loser = defender
                return winner,turns
            else:
                attacker , defender = defender , attacker
            if turns == 15:
                winner = None
                loser = None
                return None,turns
all_fights = []
round_number = 0

dragon = Creature("Dragon", 120, 30, 60, 500, 500, "water")
phoenix = Creature("Phoenix", 119, 40, 55, 500, 500, "water")
winner, turns = dragon.fight(phoenix)
round_number += 1
dic = {"round":round_number,
"creature1":dragon.name,
"creature2":phoenix.name,
"element1":dragon.element,
"element2":phoenix.element,
"winner":winner.name if winner else "Draw",
"loser":phoenix.name if winner == dragon else dragon.name if winner else None,
"winner_element":winner.element if winner else None,
"turns":turns}

all_fights.append(dic)
df = pd.DataFrame(all_fights)
print(df)