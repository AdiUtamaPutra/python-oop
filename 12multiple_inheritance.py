from ast import Pass


class A: 
    def method_A(self):
        print("Method A")

class B:
    def method_B(self):
        print("Method B")

#===== MULTIPLE INHERITANCE =======
class C(A,B):
    pass


object = C()

object.method_A()
object.method_B()