class COC:
    def __init__(self, name, hitpoint, level):
        self.name = name
        self.hitpoint = hitpoint
        self.level = level 

troops1 = COC("Barbarian",45,1)
troops2 = COC("Archer",20,1)

print(troops1.name)
print(troops1.hitpoint)
print(troops1.level)

print(troops2.name)
print(troops2.hitpoint)
print(troops2.level)