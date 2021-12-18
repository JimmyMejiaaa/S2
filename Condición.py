class condición:

    def __init__(self, num1, num2):
        self.numero1=num1
        self.numero2=num2
        numero=self.numero1+self.numero2
        self.numero3=numero

    def condición(self):
        #if ... elif ... else ...: Permiten condicionar la ejecucuión de uno o más bloques de sentencia al cumplimiento de una o varias condiciones.
        if self.numero1 == self.numero2:
            print("numero1: {} y numero2: {} son iguales".format(self.numero1, self.numero2))
        elif self.numero1 < self.numero3:
            print("numero1: {} es menor numero3: {}".format(self.numero1, self.numero2))
condi1= condición(20, 8)
print(condi1.numero3)