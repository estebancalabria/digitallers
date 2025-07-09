#Un programa en python que muestre esta escalera con dos for anidados
# *
# **
# ***
# ****
# *****
for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()
