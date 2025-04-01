def lengthchange(value, fromm, too):
    conversionvals = {"meter": 1, "kilometer": 0.001, "centimeter": 100, "millimeter": 1000,"mile": 0.000621371, "yard": 1.09361, "foot": 3.28084, "inch": 39.3701}
    return value * conversionvals[too] / conversionvals[fromm]

def weightchange(value, fromm, too):
    conversionvals2 = {"kilogram": 1, "gram": 1000, "milligram": 1000000, "pound": 2.20462,"ounce": 35.274}
    return value * conversionvals2[too] / conversionvals2[fromm]

def temperaturechange(value, fromm, too):
    fromm, too = fromm.lower(), too.lower()
    if fromm == "celsius":
        return value * 9/5 + 32 if too == "fahrenheit" else value + 273.15
    elif fromm == "fahrenheit":
        return (value - 32) * 5/9 if too == "celsius" else (value - 32) * 5/9 + 273.15
    elif fromm == "kelvin":
        return value - 273.15 if too == "celsius" else (value - 273.15) * 9/5 + 32

def bmi_calculator(weight, height):
    bmi = weight / (height ** 2)
    print(f"BMI: {bmi:.2f}")
    if bmi < 18.5:
        print("Category: Underweight")   
    elif 18.5 <= bmi < 24.9:
        print("Category: Normal weight")
    elif 25 <= bmi < 29.9:
        print("Category: Overweight")
    else:
        print("Category: Obese")

while True:
    print("Select conversion type: length, weight, temperature, bmi (or enter 0 to exit)")
    changestype = input("Enter type: ").lower().strip()
    
    if changestype == "0":
        print("Exiting program.")
        break
    
    if changestype == "length":
        value = float(input("Enter value: "))
        fromm = input("Enter from unit (millimeter, centimeter, kilometer, mile, yard, foot, inch): ").lower()
        too = input("Enter to unit (millimeter, centimeter, kilometer, mile, yard, foot, inch): ").lower()
        print("Converted value:", lengthchange(value, fromm, too))
    elif changestype == "weight":
        value = float(input("Enter value: "))
        fromm = input("Enter from unit (milligram, gram, kilogram, pound, ounce): ").lower()
        too = input("Enter to unit (milligram, gram, kilogram, pound, ounce): ").lower()
        print("Converted value:", weightchange(value, fromm, too))
    elif changestype == "temperature":
        value = float(input("Enter value : "))
        fromm = input("Enter from unit (Celsius, Fahrenheit, Kelvin): ")
        too = input("Enter to unit (Celsius, Fahrenheit, Kelvin): ")
        print("Converted value:", temperaturechange(value, fromm, too))
    elif changestype == "bmi":
        weight = float(input("Enter weight in kg: "))
        height = float(input("Enter height in meters: "))
        bmi_calculator(weight, height)
    else:
        print("Invalid conversion type")
