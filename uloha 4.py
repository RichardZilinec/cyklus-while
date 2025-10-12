cislo = int(input("zadaj cislo:"))
sum = 0
while cislo !=0:
    o = cislo % 10
    cislo//=10
    print(o,end='')