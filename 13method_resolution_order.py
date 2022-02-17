class A:
    def show(self):
        print("Show A")

class B:
    def show(self):
        print("Show B")

class C(A,B):
    def show(self):
        print("Show C")


object = C()
object.show()


# METHOD RESOLUTION ORDER(urutan pemanggilan method dari class inheritance)
# Jika nama method dimasing-masing class sama, method mana yang dipanggil duluan ?
# Urutan Pemanggilan = 
                      # I Class C 
                      # II Class A 
                      # III Class B
help(object) 




