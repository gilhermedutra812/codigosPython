for cont in range(1,11):
    print(cont, " ",end=" ")# impedindo de quebrar linha

for cont in range(1,21,3):
    print (cont)

for cont in range(11,1, -1):
    print(cont, "-", end="")

for cont in range (1,11):
    print("-"*15,"VALORES PARES","-"*15)
    if cont %2 == 0:
        print(cont," ", end="")
