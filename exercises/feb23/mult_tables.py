#Authr: Avery Cordle

tableSize = int(input("What number table do you want? "))

for row in range(1, tableSize + 1): #loop through rows
    
    for col in range(1, tableSize + 1): #for every row, loop through cols
        answer = row*col
        if (len(str(answer)) == 1):
            print(f" {answer}", end = " ")
        else:
            print(f"{answer}", end = " ")
        
    print()



















