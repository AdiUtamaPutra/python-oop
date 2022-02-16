class COC:
    #private class variable
    __jlm = 0

    def __init__(self, name):
        self.__name = name
        COC.__jlm += 1

    #method ini hanya berlaku untuk object
    def getJumlah(self):
        return COC.__jlm

    #method ini tidak berlaku untuk object tapi berlaku untuk class
    def getJumlah2():
        return COC.__jlm

    #method ini berlaku untuk object dan class
    @staticmethod
    def getJumlah3():
        return COC.__jlm

    @classmethod
    def getJumlah4(cls):  # -> sama dgn statucmethod, perbedaannya hanya menggunakan argumen.
        return cls.__jlm


#object
troops = COC('Barbarian')

print(troops.getJumlah())
print(COC.getJumlah2())

print(COC.getJumlah3())
print(troops.getJumlah3())

print(COC.getJumlah4())
