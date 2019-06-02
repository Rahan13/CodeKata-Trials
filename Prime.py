a= int(input())
count = 0
for i in range(1,a+1):
    if(a%i == 0):
        count += 1
    if(count>2):
        break
if(count==2):
    print("yes")
else:
    print("no")
