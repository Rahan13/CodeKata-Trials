def selectClock(r,c):
    l=list()
    for i in range(c,c+3):
        l.append(mat[r][i])
    l.append(mat[r+1][c+1])
    r=r+2
    for i in range(c,c+3):
        l.append(mat[r][i])
    return (sum(l),l)

def process():
    for i in range(0,row-2):
        for j in range(0,column-2):
            s,l=selectClock(i,j)
            d.update({s:l})
    if len(d.keys())!=0:
        sorted(d.keys())
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
