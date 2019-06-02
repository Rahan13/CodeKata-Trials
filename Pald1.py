
a= int(input())
b=a
c=0
while(int(b)>0):
    d=int(b)%10
    c=(c*10)+d
    b/=10
print(c)
