cislo = int(input("zadaj cislo:"))
parne = 0
neparne = 0
sum = 0

while cislo !=0:
    t = cislo % 10
    cislo//=10
    #print(t,end='')
    sum*=10
    sum+= t
    
cislo = sum
cislo2 = sum

print ("parne cisla su:",end='')
while cislo !=0:
    o = cislo % 10
    cislo//=10
    neparne = o
    cislo//=10
    print(neparne,end='')
print ("")
print ("neparne cisla su:",end='')
while cislo2 !=0:
    o = cislo2 % 100
    cislo2//=100
    parne = o//10
    print(parne,end='')