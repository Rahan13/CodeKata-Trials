import java.util.*;

public class Trial5{
    static int a;
    static void getData(){
    Scanner s =  new Scanner(System.in);
    a = s.nextInt();
    s.close();
    }
    static void compute(){
        if(a%4==0)
        System.out.println("yes");
        else
        System.out.println("no");
    }
     public static void main(String []args){
        getData();
        compute();
     }
}
