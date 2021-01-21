#Author: Avery Cordle 
import math
#Age predictor
age = float(input("Enter age: "))
decade = 10
futureAge = age + decade

print(f"""You are {age} years old.
In a decade you will be {futureAge} years old.""")

#pizza party
numGuest = int(input("Enter number of guests: "))
slicesPerGuest = 2.5
totalSlices = numGuest * slicesPerGuest
numPizzas = totalSlices/6
#float division will be precise and result in a decimal
#integer devision (ex: //) will cut off the decimal

#numPizzas = round(numPizzas,0)
#round (variable, decimal places)... round(3.75,1) = 3.8
numPizzas = math.ceil(numPizzas)
#floor and ceil (you have to import math to use these)

print(f"""You are having {numGuest} people at your party.
You will need {totalSlices} number of pizza slices, 
and {numPizzas} pizzas.""")


#chickens
numEggs = 57
numCartons = numEggs//12
print(f"You need {numCartons} cartons of eggs.")


#traveling
milesTraveling = float(input("Enter miles traveling: "))
pricePerMile = float(input("Enter price per mile: "))
priceToTravel = round(milesTraveling * pricePerMile,2)
print(f"You will be charged ${priceToTravel}")







