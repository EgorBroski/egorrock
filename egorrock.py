from keyboard import*
print("Kivi, Käärid, Paber")
while True:
    try:
        if read_key()=="k":
            print("Oli valitud kivi")
            break
    except:
        ValueError
v1=["Kivi","Käärid","Paber"]
v2=["Kivi","Käärid","Paber"]
if m==1:
    while 1:
        print("Mängime")
        v=input()
        if v=="no":break
        if read_key()=="N": break
        p1=choice(v1)
        print("Esimene bot: ",p1)
        p2=choice(v2)
        print("Teine bot: ",p2)
        if p1==p2: print("Viik")
        if p1==v1[0] and p2==v2[1] or p1==v1[2] and p2==v2[0] or p1==v1[1] and p2==v2[2]:
            print("Võitis 1")
        else:
            print("Võitis 2")
v1=["Kivi","Käärid","Paber"]
v2=["Kivi","Käärid","Paber"]
if m==1:
    while True:
        print("Kas mängime? esc - välja, enter - mängime")
        if read_key()=='esc':
            break
        elif read_key()=='enter':
            p1=choice(v1)
            print("Esimene bot: ",p1)
            p2=choice(v2)
            print("Teine bot: ",p2)
            if p1==p2:
                print("Viik")
            if p1==v1[0] and p2==v2[1] or p1==v1[2] and p2==v2[0] or p1==v1[1] and p2==v2[2]:
                print("Võitis 1")
            else:
                print("Võitis 2")
m=3
while m not in [1,2]:
    try:
        m=int(input("Kellega mängime?\n1-inimesega\n2-robotiga\nKirjuta vastus:"))
    except:
        ValueError
if m==1:
    while 1:
        pass
elif m==2:
    while 1:
       pass







