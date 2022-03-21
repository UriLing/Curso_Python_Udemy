#clase 66,67

class aritmetica():
    def __init__(self,operandoA, operandoB):
        self.operandoA = operandoA
        self.operandoB = operandoB
    
    def sumar(self):
        return self.operandoA + self.operandoB
    
    def restar(self):
        return self.operandoA - self.operandoB
    
    def multiplicar(self):
        return self.operandoA * self.operandoB
    def division(self):
        return self.operandoA / self.operandoB

aritmetica1 = aritmetica(5,5)
print(aritmetica1.sumar())