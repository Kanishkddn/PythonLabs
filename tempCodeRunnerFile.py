class Calc:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def mul(self):
        return self.a * self.b

    def div(self):
        if self.b != 0:
            return self.a / self.b
        else:
            return "Division by zero is not allowed"
    
    def pow(self):
        return self.a**self.b
        
a = int(input("Enter First number: "))
b = int(input("Enter Second number: "))


calculator = Calc(a, b)


print("Addition:", calculator.add())
print("Subtraction:", calculator.sub())
print("Multiplication:", calculator.mul())
print("Division:", calculator.div())
print("Exponent:", calculator.pow())
