cislo = int(input("zadaj cislo:"))
sum = 0
cislo2 = cislo

while cislo !=0:
    o = cislo % 10
    cislo//=10
    #print(o)
    sum+=1
#print("pocet cisel je:",sum)

if sum%2!=0:
    #print("je neparne")
    o = (sum//2)+1
    for i in range (1,o):
        cislo2//=10
    t = cislo2%10
    print("stredna cifra je",t)
else:
    #print("je parne")
    o = (sum//2)
    for i in range (1,o):
        cislo2//=10
    t = cislo2%10
    f = (cislo2//10)%10
    print("stredna cifra je",(t+f)/2)