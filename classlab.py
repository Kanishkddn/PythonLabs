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

'''2'''
class Temp:
    def __init__(self, value, fromm, too):
        self.value = value
        self.fromm = fromm.lower()
        self.too = too.lower()

    def temperaturechange(self):
        if self.fromm == "celsius":
            if self.too == "fahrenheit":
                return self.value * 9/5 + 32
            elif self.too == "kelvin":
                return self.value + 273.15
        elif self.fromm == "fahrenheit":
            if self.too == "celsius":
                return (self.value - 32) * 5/9
            elif self.too == "kelvin":
                return (self.value - 32) * 5/9 + 273.15
        elif self.fromm == "kelvin":
            if self.too == "celsius":
                return self.value - 273.15
            elif self.too == "fahrenheit":
                return (self.value - 273.15) * 9/5 + 32

        return "Invalid conversion units"

value = float(input("Enter value for conversion: "))
fromm = input("Enter from unit (Celsius, Fahrenheit, Kelvin): ")
too = input("Enter to unit (Celsius, Fahrenheit, Kelvin): ")

tempyy = Temp(value, fromm, too)
result = tempyy.temperaturechange()

print(f"Converted {value} {fromm} to {too} : {result}")

'''3'''

class LengthConverter:
    def __init__(self, value, fromunit, tounit):
        self.value = value
        self.fromunit = fromunit.lower()
        self.tounit = tounit.lower()

    def convert(self):
        conversionfactors = {
            "meter": 1, "kilometer": 0.001, "centimeter": 100, "millimeter": 1000,
            "mile": 0.000621371, "yard": 1.09361, "foot": 3.28084, "inch": 39.3701
        }

        if self.fromunit not in conversionfactors or self.tounit not in conversionfactors:
            return "Invalid unit entered!"

        return self.value * conversionfactors[self.tounit] / conversionfactors[self.fromunit]

value = float(input("Enter value for length unit conversion: "))
fromunit = input("Enter unit to convert from (meter, kilometer, centimeter, millimeter, mile, yard, foot, inch): ")
tounit = input("Enter unit to convert to (meter, kilometer, centimeter, millimeter, mile, yard, foot, inch): ")

converter = LengthConverter(value, fromunit, tounit)
result = converter.convert()

print(f"Converted {value} {fromunit} to {tounit}: {result}")
