# Task 3.1

# Creating a list of icecream and empty list
flavours = ['vanilla', 'chocolate', 'caramel', 'maple', 'strawberry', 'rasperry', 'strife', 'magnum']
flavourLengths = []

# The For Loop
for icecream in range(1,8):
    print(flavours[icecream])
    print(flavours[icecream].upper())
    flavourLengths.append(len(flavours[icecream]))
print(flavourLengths)

