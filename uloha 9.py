cislo = int(input("zadaj cislo:"))
sum = 0
cislo2 = cislo

while cislo !=0:
    t = cislo % 10
    cislo//=10
    #print(t,end='')
    sum*=10
    sum+= t
if sum == cislo2:
    print("cislo je symetricke")
else:
    print("cislo nie je symetricke")
