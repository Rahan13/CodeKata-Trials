a= int(input())
b=a
c=0
while(a>0):
    d = a%10
    c = c + d**3
    a = int(a/10)
if(c==b):
    print("yes")
else:
    print("no")
