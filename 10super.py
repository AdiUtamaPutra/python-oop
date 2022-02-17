class COC:
    def __init__(self,name,hitpoint):
        self.name = name
        self.hitpoint = hitpoint

    def info(self):
        print("{} dengan hitpoint: {}".format(self.name,self.hitpoint))


class Attacker(COC):
    def __init__(self,name):

        # COC.__init__(self, name, 20)
        # COC.info(self)
                    #or
        super().__init__(name,20)
        super().info()


class Defense(COC):
    def __init__(self,name):

        # COC.__init__(self, name, 40)
        # COC.info(self)
                    #or
        super().__init__(name,40)
        super().info()



troops1 = Attacker('Wizard')
troops2 = Defense('Wizard Tower')

        