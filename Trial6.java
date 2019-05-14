import java.util.*;
public class Trial5{
    static int a;
    static void getData(){
    Scanner s =  new Scanner(System.in);
    a = s.nextInt();
    s.close();
    }
    static void compute(){
       for(int i=0;i<a;i++)
       System.out.println("Hello");
    }
     public static void main(String []args){
        getData();
        compute();
     }
}
