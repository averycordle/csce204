#Author: Avery Cordle

#learning lists
#so we want to store a list of data -> we will use a list

toys = ["doll","truck","car","train","crayons"]

toys.append("phone")
toys.append("marker")
toys.append("bottle")
toys.append("soda")
toys.append("ball")

"""
#display all the items in the list
for i in range(10):
    print(toys[i])
"""

#remove
if "doll" in toys:
    toys.remove("doll")


#in this situation toy becomes i 
for toy in toys:
    print(toy)

