import java.util.*;

public class Trial3{
    
static String a;
    
static String str ="aeiou";
    
static void getData(){
    
Scanner s =  new Scanner(System.in);
    
a = s.next();
    
s.close();
    
}
    
static void compute(){
        
if(str.contains(a))
        
System.out.println("Vowel");
        
else
        
System.out.println("Consonant");
    
}
     
public static void main(String []args){
        
getData();
        
compute();
     
}
}