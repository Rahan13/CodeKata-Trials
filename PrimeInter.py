a= input().split()
for i in range(int(a[0]),int(a[1])):
    count1 = 0
    count2 = 0
    for j in range(1,i+1):
        if(i%j == 0):
            count1 += 1
    if count1==2:
        count2 += 1
print(count2)
