class COC:
    #class variable 
    jlm = 0

    def __init__(self, name, hitpoint, level):
        #instance variable
        self.name = name
        self.hitpoint = hitpoint
        self.level = level 

        COC.jlm += 1
        print("Create troops = " + name)


troops1 = COC("Barbarian",45,1)
print(COC.jlm)
troops2 = COC("Archer",20,1)
print(COC.jlm)
