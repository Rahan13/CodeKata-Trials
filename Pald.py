
a= int(input())
b = a
c=0
while(b>0):
    d=b%10
    c=(c*10)+d
    b=int(b/10)
if(c==a):
    print("yes")
else:
    print("no")
