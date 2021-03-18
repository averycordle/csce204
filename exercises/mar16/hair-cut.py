#Author: Avery Cordle

#gender = m or f
#length = l or s
#density = t or th
def get_cut_cost(gender, length, density):
    price = 0

    #price based on gender
    if gender == "m":
        price += 20
    else:
        price += 40
    
    #price based on length
    if length == "l":
        price += 10

    #price based on thickness
    if density == "t":
        price += 15
    
    return price

#length = l or s
#density = t or th
#change = l or d
def get_color_cost(length, density, change):
    basePrice = 100

    if length == "l":
        basePrice += 40
    
    if density == "t":
        basePrice += 60
    
    if change == "l":
        basePrice += 50

    return basePrice

print("Salon Services")
print("Price Estimation Calculation")
gender = input("Gender (M)ale or (F)emale: ").lower().strip()
hairLength = input("Length (L)ong or (S)hort: ").lower().strip()
hairDensity = input("Density (T)hick or (Th)in: ").lower().strip()
hairCut = input("Do you want your hair cut (Y)es or (N)o: ").lower().strip()
hairColor = input("Do you want your hair colored (Y)es or (N)o: ").lower().strip()

cost = 0

if hairCut == "y":
    cost += get_cut_cost(gender, hairLength, hairDensity)

if hairColor == "y":
    colorChange = input("Will you be going (L)ighter or (D)arker: ").lower().strip()
    cost += get_color_cost(hairLength, hairDensity, colorChange)

cost *= 1.07
print(f"Your estimated total is ${round(cost,2)}")