cislo = int(input("zadaj cislo:"))
sum = 0
while cislo !=0:
    o = cislo % 10
    cislo//=10
    #print(o)
    if (o >> 0) and (o%2==0):
        sum+=1
    else:
        sum+=0
print("pocet parnych cisel je:",sum)