import tornado


class COC:
    def __init__(self,name,hitpoint):
        self.name = name
        self.hitpoint = hitpoint

    def info(self):
        print("Name: {}, hitpoint: {}".format(self.name, self.hitpoint))


class Attacker(COC):
    def __init__(self,name):
        super().__init__(name,21)

    #====== OVERRIDE ======
    def info(self):
        print("Name: {}, hitpoint: {}, Type: Attacker".format(self.name, self.hitpoint))


class Defense(COC):
    def __init__(self,name):
        super().__init__(name,200)
        

troops = Attacker("Golem")
troops2 = Defense("Barbarian King")

troops.info()
troops2.info()