import java.util.*;
interface Compute{void convert();}
class GB implements Compute{
    long g; GB(long g){this.g=g;}
    public void convert(){System.out.println(g+" GB = "+(g*1024L*1024*1024)+" Bytes");}
}
class Euro implements Compute{
    double e; Euro(double e){this.e=e;}
    public void convert(){System.out.println(e+" Euro = "+(e*90)+" Rupees");}
}
class Main{
    public static void main(String[] a){
        Scanner s=new Scanner(System.in);
        System.out.print("Enter GB: ");
        Compute c1=new GB(s.nextLong());
        System.out.print("Enter Euro: ");
        Compute c2=new Euro(s.nextDouble());
        c1.convert(); c2.convert();
        s.close();
    }
}
