class COC:

    def __init__(self,name, hitpoint):
        self.__name = name
        self.__hitpoint = hitpoint


    @property
    def hitpoint(self):
        pass

    @hitpoint.getter
    def hitpoint(self):
        return self.__hitpoint
    @hitpoint.setter
    def hitpoint(self,val):
        self.__hitpoint += val
    @hitpoint.deleter
    def hitpoint(self):
        self.__hitpoint = None
        

troops = COC("Barbarian",20)

# ========= Getter & Setter ========
print(troops.hitpoint)  #->getter

troops.hitpoint = 20    #->setter
print(troops.hitpoint)

# ========== Deleter =========
del troops.hitpoint
print(troops.__dict__)