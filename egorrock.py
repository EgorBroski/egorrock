from keyboard import*
print("Kivi, Käärid, Paber")
while True:
    try:
        if read_key()=="k":
            print("Oli valitud kivi")
            break
    except:
        ValueError
m=3
while m not in [1,2]:
    try:
        m=int(input("Kellega mängime?\n1-inimesega\n2-robotiga"))
    except:
        ValueError
if m==1:
    while 1:
        print("Mängime inimesega")
        break
elif m==2:
    while 1:
        print("Mängime robotiga")
        break
print("Mida valid?")
vibor=int(input("Kivi-1,Käärid-2,Paber-3"))
if vibor=="1":



