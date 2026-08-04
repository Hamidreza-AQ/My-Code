"""Mew! Mew!"""
class VirtualCat:
# functions
    def __init__(self,name):
#                     str
        self.name = name
        self.hunger = 50
        self.energy = 50
        self.boredom = 50
        self.is_alive = True
        
    def status(self):
        return f"name : {self.name} / hunger : {self.hunger} / energy : {self.energy} / boredom : {self.boredom}"
    
    def feed(self):
        if self.is_alive == True:
            self.energy = self.energy - 5
            self.hunger = self.hunger - 20
            if self.hunger < 0:
                self.hunger = 0
            if self.energy < 0:
                self.energy = 0
            return "num num num!"
        
    def play(self):
        if self.is_alive == True:
            self.boredom = self.boredom - 15
            if self.boredom < 0:
                self.boredom = 0
            self.energy = self.energy - 10
            self.hunger = self.hunger + 5
            if self.energy < 0:
                self.energy = 0
            if self.hunger >= 100 or self.energy <= 0:
                self.is_alive = False
                return f"{self.name} mord! (barash fatehe bekhonid)"
            return "mi param va gaz migiram! "
    
    def sleep(self):
        if self.is_alive == True:
            if (self.energy + 20) < 100:
                self.energy = self.energy + 20
                
            else:
                self.energy = 100
            self.hunger = self.hunger + 10
            return "khkhkhkhkh, poofffff..."
        
    def tick(self):
        self.hunger = self.hunger + 5
        self.energy = self.energy - 3
        self.boredom = self.boredom + 4
        
        if self.hunger >= 100 or self.energy <= 0:
            self.is_alive = False
            return f"{self.name} mord! (barash fatehe bekhonid)"
        
    def auto_pilot(self):
        if self.is_alive == True:
            
            if self.hunger > 70:
                self.feed()
            elif self.boredom > 70:
                self.play()
            elif self.energy < 20:
                self.sleep()
            else:
                self.tick()
    
    def mew(self):
        if self.is_alive == True:
            self.boredom - 5
            if self.hunger >= 100 or self.energy <= 0:
                self.is_alive = False
                return f"{self.name} mord! (barash fatehe bekhonid)"
            return "mew! mew!"

#TEST
input_ = input("Gorbe name : ")
keke = VirtualCat(f"{input_}")

#loop
while keke.is_alive == True:
    k = int(input("""
1.feed
2.play
3.sleep
4.status
5.mew mew
6.auto pilot
7.tick
0.exit
adad ra vared konid: """))
    
    if k > 7 or k < 0:
        print("invalid input")
        
    if k == 1:
        print(keke.feed())
        
    if k == 2:
        print(keke.play())
        
    if k == 3:
        print(keke.sleep())
        
    if k == 4:
        print(keke.status())
        
    if k == 5:
        print(keke.mew())
    
    if k == 6:
        print(keke.auto_pilot())
        
    if k == 7:
        print(keke.tick())
        
    if k == 0:
        print("khoda negahdar!")
        
    if k == 1 or k == 2 or k == 3 or k == 4 or k == 5 or k == 6 or k == 7:
        print(keke.status())
    
    if keke.is_alive == False:
        print("RIP keke...")