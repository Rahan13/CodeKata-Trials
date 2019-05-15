y=True
count =0
while(y):
    a=str(input("Enter the inputs:"))
    alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    b=a.split()
    if b[0] in alpha or b[1] in alpha:
        print("Error")
        count=count+1
    else:
        c=int(input("1.Addition 2.Sub 3.Mul 4.Div "))
        if(c==1):
            print(int(b[0])+int(b[1]))
        elif(c==2):
            print(int(b[0])-int(b[1]))
        elif(c==3):
            print(int(b[0])*int(b[1]))
        elif(c==4):
            if(float(b[1])==0.0):
                print("Div by zero exception")
            else:
                print(float(b[0])/float(b[1]))
        else:
            count+=1
    if(count>=4):
        y=False
    
    
    
