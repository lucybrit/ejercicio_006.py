#radio_circulo=float(input("Ingresa el radio del circulo: "))
#altura_cilindro=float(input("Ingresa la altura del cilindro: "))
pi=3.1416

class Cilindro:

    def __init__ (self, radio, altura):
        self.radio=radio
        self.altura=altura

    def __str__ (self):
        return f"El area del cilindro es igual a {((pi*self.radio)**2)}"

c1=(Cilindro(10,20))

print  (c1)


    



