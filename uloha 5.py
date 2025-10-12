cislo = int(input("zadaj cislo:"))
cislo2 = cislo
parne = 0
neparne = 0
print ("neparne cisla su:",end='')
while cislo !=0:
    o = cislo % 10
    cislo//=10
    neparne = o
    print(neparne,end='')
    cislo//=10
print ("")
print ("parne cisla su:",end='')
while cislo2 !=0:
    o = cislo2 % 100
    cislo2//=100
    parne = o//10
    print(parne,end='')