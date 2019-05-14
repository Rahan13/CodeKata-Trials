import java.util.*;

public class Trial4{
    
static String a;
    
static String str ="abcdefghijklmnopqrstuvxyz";
    
static void getData(){
    
Scanner s =  new Scanner(System.in);
    
a = s.next();
    
s.close();
    
}
    
static void compute(){
        
a.toLowerCase();
        
if(str.contains(a))
       
System.out.println("Alphabet");
       
else
        
System.out.println("No");
    
}
     
public static void main(String []args){
        
getData();
        
compute();
     
}
}