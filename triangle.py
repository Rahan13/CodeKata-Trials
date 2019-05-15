def spacing(b):
    while(b>1):
        print(" "),
        b=b-1
a=int(input())
j=int(input())
i=1
for i in range(1,a):
    b=(a-i)
    spacing(b)
    c=i
    while(c>0):
        print(i*j),
        #print("*"),
        print(" "),
        c=c-1
    print("")
