a= input().split()
for i in range(int(a[0]),int(a[1])):
    count = 0
    for j in range(1,i+1):
        if(i%j == 0):
            count += 1
    if count==2:
        print(i, end = " ")
