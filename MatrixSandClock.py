def selectClock(r,c,k):
    l=list()
    for i in range(c,c+k):
        l.append(mat[r][i])
    l.append(mat[r+int(k/2)][c+int(k/2)])
    r=r+(k-1)
    for i in range(c,c+k):
        l.append(mat[r][i])
    return (sum(l),l)

def process():
    if row%2 !=0 and row>=3:
        k=row
    while(k>=3):
        for i in range(0,row-k+1):
            for j in range(0,column-k+1):
                s,l=selectClock(i,j,k)
                d.update({s:l})
        k=k-2
    if len(d.keys())!=0:
        l1=d.keys()
        print(max(l1),d[max(l1)])
    else:
        print("No value")
    
row,column=input().split()
row=int(row)
column=int(column)
mat=list(list())
for i in range(row):
    c=input().split()
    c=list(map(int,c))
    mat.append(c)
d=dict()
process()
