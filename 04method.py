class COC:
    #class variable
    jlm_troops = 0

    def __init__(self,name,hitpoint,damage,armor,level):
        #instance variable
        self.name = name
        self.hitpoint = hitpoint
        self.damage = damage
        self.armor = armor
        self.level = level

        COC.jlm_troops += 1

    #method without return and argument
    def sayHai(self):
        print('myname is ' + self.name)

    #method with argument, without return
    def hitpointUp(self, up):
        self.hitpoint += up

    #method with return
    def getHitpoint(self):
        return self.hitpoint


troops1 = COC('Barbarian',45,7,2,1)
troops2 = COC('Archer',20,7,1,1)

#calling method sayHai()
troops1.sayHai()
troops2.sayHai()

#calling method hitpointUp()
troops1.hitpointUp(10)
print(troops1.hitpoint)

#calling method getHitpoint()
print(troops2.getHitpoint())       