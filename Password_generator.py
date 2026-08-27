import random
small = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
big = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
numbers = ["0","1","2","3","4","5","6","7","8","9"]
characters = [".",".","_"]
i = int(input("Number of characters required: "))
n = 0
password = ""
while n!= i:
    s = random.choice(small)
    b = random.choice(big)
    num = random.choice(numbers)
    c = random.choice(characters)
    l = [s,b,num,c]
    password = password + random.choice(l)
    n = n + 1
print(password)