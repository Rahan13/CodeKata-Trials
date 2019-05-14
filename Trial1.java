import java.util.*;
public class Trial1{   
static int a;   
static void getData(){   
Scanner s =  new Scanner(System.in);
a = s.nextInt();    
s.close();    
}
    
static void compute(){       
if(a>0)        
System.out.println("Positive");        
else if(a==0)        
System.out.println("Zero");        
else       
System.out.println("Negative");    
}
     
public static void main(String []args){        
getData();        
compute();     
}
}
