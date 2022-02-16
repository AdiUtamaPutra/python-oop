#syarat :
    # 1. Buat semua variable private
    # 2. Getter -> mengambil var
    # 3. Setter -> meng-set var


class COC:
    def __init__(self, name, hitpoint):
        self.__name = name
        self.__hitpoint = hitpoint

    #getter
    def getName(self):
        return self.__name
    def getHitpoint(self):
        return self.__hitpoint

    #setter
    def hitpointUp(self, val):
        self.__hitpoint += val


troops = COC('Barbarian',20,2)

#getter
print(troops.getName())

#setter
troops.hitpointUp(10)
print(troops.getHitpoint())