a = input().split()
count=0
if (len(a[0])== len(a[1])):
    for i in range(0,len(a[0])):
        if(a[0][i]!=a[1][i]):
            count += 1
        if(count>1):
            print("no")
            break
    if(count==1):
        print("yes")
else:
    print("no")
