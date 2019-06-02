a= input()
b = input().split()
c = []
ind = 0
for i in range(0,len(b)):
    if b.count(b[i])>1 and not(b[i] in c):
        print("inserting",b[i])
        c.insert(ind,b[i])
        ind += 1
c.sort()
for i in range(0,len(c)):
    print(int(c[i]), end = " ")
