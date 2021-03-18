#Author: Avery Cordle

def fahr_to_cels(fahrenheit):
    celcius = (fahrenheit - 32) * 5/9
    return celcius

def cels_to_fahr(celcius):
    fahrenheit = (celcius * 9/5) + 32
    return fahrenheit

def miles_to_kilos(miles):
    kilos = miles * 1.609
    return kilos
    
def kilos_to_miles(kilos):
    miles = kilos/1.609
    return miles

command = int(input(f"""
Enter Type of Conversion
1.Fahrenheit to Celcius
2.Celcius to Fahrenheit
3.Miles to Kilometer
4.Kilometer to Miles
"""))

if command > 4 or command < 1:
    print("Invalid Command")
else:
    value = float(input("Enter value:"))

    if command == 1:
        celcius = fahr_to_cels(value)
        print(f"{value} fahrenheit is {round(celcius,2)} celcius")
    elif command == 2:
        fahrenheit = cels_to_fahr(value)
        print(f"{value} celcius is {round(fahrenheit,2)} fahrenheit")
    elif command == 3:
        kilos = miles_to_kilos(value)
        print(f"{value} miles is {round(kilos,2)} kilometers")
    elif command == 4:
        miles = kilos_to_miles(value)
        print(f"{value} kilometers is {round(miles,2)} miles")