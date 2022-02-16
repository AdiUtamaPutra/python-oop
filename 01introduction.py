class COC:  #template
    pass


troops_1 = COC()   #object/instance
troops_2 = COC()


troops_1.name = 'Barbarian'
troops_1.hitpoints = 45
troops_1.level = 1

troops_2.name = 'Archer'
troops_2.hitpoints = 20
troops_2.level = 1


print(troops_2.name)