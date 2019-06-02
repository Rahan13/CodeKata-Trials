a= input().split()

for i in range(int(a[0]),int(a[1])):
    b=i
    c=0
    while(i>0):
        d = i%10
        c = c + d**3
        i = int(i/10)
    if(c==b):
        print(c, end = " ")

