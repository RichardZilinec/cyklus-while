cislo = int(input("zadaj cislo:"))
i = 1

print("delitele cisla su:")
while (i<cislo+1):
    #print(i,end=',')
    if cislo % i == 0:
        print(i,end=',')
    i+=1
