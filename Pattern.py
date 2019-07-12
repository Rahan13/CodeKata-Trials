num=input()
try:
    num=int(num)
    if num<=0:
        print("Unexpected Exit!")
    else:
        for i in range(num):
            if i==0:
                print(" ",end="")
            for j in range(num-i):
                print(" ",end="")
            for k in range(i+1):
                print(k+1,end=" ")
            if i!=0:
                print(i-(i-1))
            else:
                print("")
        i=num-1
        while(i>0):
            if i==1:
                print(" ",end="")
            for j in range(num+1-i):
                print(" ",end="")
            for k in range(i):
                print(k+1,end=" ")
            if i!=1:
                print(i-(i-1))
            else:
                print("")
            i =i-1
except Exception:
    print("Float value found!")
