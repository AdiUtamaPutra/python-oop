from msilib.schema import Class


class A():
    def show(self):
        print("Method A")

class B(A):
    def show(self):
        print("Method B")

class C(A):
    def show(self):
        print("Method C")

class D(B,C):
    pass


object = D()
object.show()

help(object)
# Urutan pemanggilan : class D -> class B -> class C -> class A 