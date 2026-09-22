class VirtualPlant():
    def __init__(self,name):
        self.name = name
        self.water = 50
        self.sunlight = 50
        self.fertilizer = 50
        self.health = 100
        self.growth_stage = "seed"
        self.age = 0
        self.is_alive = True

    def status(self):
        return f"""
Name : {self.name} 
Water = {self.water}
Sunlight = {self.sunlight}
Fertilizer = {self.fertilizer}
Health = {self.health}
Growth_stage = {self.growth_stage}
Age = {self.age}
Is alive = {self.is_alive}"""

    def water_plant(self,meghdar):
        self.water += meghdar
        if self.water > 100:
            self.water = 100
        if self.water < 0:
            self.water = 0
        #اثر جانبی
        return "آب به گیاه اضافه شد"
    
    def give_sunlight(self,meghdar):
        self.sunlight += meghdar
        if self.sunlight > 100:
            self.sunlight = 100
        if self.sunlight < 0:
            self.sunlight = 0
        return "نور به گیاه رسید"

    def add_fertilizer(self, meghdar):
        self.fertilizer += meghdar
        if self.fertilizer > 100:
            self.fertilizer = 100
        if self.fertilizer < 0:
            self.fertilizer = 0
        return "به گیاه کود داده شد"

    def update_health(self):
        b1 = (40 < self.water < 70)
        b2 = (40 < self.sunlight < 70)
        b3 = (30 < self.fertilizer < 60)

        if 40 < self.water < 70 and 40 < self.sunlight < 70 and 30 < self.fertilizer < 60:
            self.health += 10

        if b1 == False or b2 == False or b3 == False:
            self.health -= 5

        if self.water == 0 or self.water == 100 or self.sunlight == 0 or self.sunlight == 100 or self.fertilizer == 0 or self.fertilizer == 100:
            self.health -= 15

        if self.health > 100:
            self.health = 100
        if self.health < 0:
            self.health = 0

    def grow(self):
        health = self.health >= 50
        if 0 <= self.age <= 2 and health == True:
            self.growth_stage = "seed"

        elif 3 <= self.age <= 5 and health == True:
            self.growth_stage = "sprout"

        elif 6 <= self.age <= 10 and health == True:
            self.growth_stage = "seedling"

        elif 11 <= self.age <= 20 and health == True:
            self.growth_stage = "mature" 

        elif self.age > 21 and health == True:
            self.growth_stage = "flowering"

    def check_alive(self):
        if self.health <= 0:
            self.is_alive = False

    def next_day(self):
        self.age += 1
        self.water -= 10
        self.sunlight -= 5
        self.fertilizer -= 2

        if self.water > 100:
            self.water = 100
        if self.water < 0:
            self.water = 0

        if self.sunlight > 100:
            self.sunlight = 100
        if self.sunlight < 0:
            self.sunlight = 0

        if self.fertilizer > 100:
            self.fertilizer = 100
        if self.fertilizer < 0:
            self.fertilizer = 0

        self.update_health()
        self.grow()
        self.check_alive()
        
        if self.health > 100:
            self.health = 100
        if self.health < 0:
            self.health = 0
        return f"Day : {self.age} | Growth Stage : {self.growth_stage}"

    def get_growth_data(self):
        dic = {
"day": self.age,
"health": self.health,
"water": self.water,
"sunlight": self.sunlight,
"fertilizer": self.fertilizer,
"stage": self.growth_stage}
        return dic 

#Test
p1 = VirtualPlant("googooly")
p1.water_plant(26)
p1.status()
p1.give_sunlight(26)
p1.next_day()
p1.next_day()
p1.next_day()
p1.update_health()
print(p1.status())