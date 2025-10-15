cislo = int(input("zadaj cislo:"))
while cislo > 1:
    if cislo%2==0:
        cislo//=2
    else:
        cislo = cislo*3+1
    print(cislo,end=',')
