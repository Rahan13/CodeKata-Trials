import java.util.*;

public class Trial2{
    
static int a;
    
static void getData(){
    
Scanner s =  new Scanner(System.in);
    
a = s.nextInt();
    
s.close();
    
}
   
static void compute(){
        
if(a%2==0)
        
System.out.println("Even");
       
else if(a%2!=0)
        
System.out.println("Odd");
        
else
        
System.out.println("Invalid");
    
}
     
public static void main(String []args){
        
getData();
        
compute();
     
}
}