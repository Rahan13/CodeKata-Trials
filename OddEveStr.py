a= input()
b = list(a)
leng = len(b)
if(len(b)%2!=0):
 leng = leng-1
for i in range(0,leng):
    if(i%2 == 0):
        print(b[i+1], end = "")
    else:
        print(b[i-1], end = "")
if(len(b)%2 != 0):
    print(b[leng])
