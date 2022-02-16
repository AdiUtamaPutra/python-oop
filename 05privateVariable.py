class COC:
    #class variable public
    jlm = 0 

    #class variable private
    __privateClass = "classPrivate"

    #class variable protected
    _protectedClass = "protectedClass"
    

    def __init__(self,name,hitpoint):
        #variable instance public
        self.name = name
        self.hitpoint = hitpoint

        #variable instance private
        self.__damage = "damage"

        #variable instance protected
        self._level = "level"


troops = COC("Wizard",30)


#class variable public
print(COC.jlm)
#class variable private
print(COC.__privateClass)
#class variable protected
print(COC._protectedClass)

#variable instance public
print(troops.name)
#variable instance private
print(troops.__damage)
#variable instance protected
print(troops._level)
