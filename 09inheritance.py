class COC:

    def __init__(self,name,hitpoint):
        self.name = name
        self.hitpoint = hitpoint

class Attacker(COC):
    pass

class Defense(COC):
    pass

troops1 = COC('Goblin',10)
troops2 = Attacker('Barbarian',20)
troops3 = Defense('Archer Tower',50)

print(troops1.name)
print(troops2.name)
print(troops3.name)

