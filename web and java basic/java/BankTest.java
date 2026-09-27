import java.util.*;
abstract class Bank{
    String n; int acc; double b;
    void read(Scanner s){
        System.out.print("Enter name: "); n=s.next();
        System.out.print("Enter account number: "); acc=s.nextInt();
        System.out.print("Enter balance: "); b=s.nextDouble();
    }
    void show(){ System.out.println(n+" "+acc+" "+b); }
    abstract void roi();
}
class City extends Bank{
    void roi(){ System.out.println("CityBank Interest: "+b*0.06); }
}
class SBI extends Bank{
    void roi(){ System.out.println("SBI Interest: "+b*0.07); }
}
class Canara extends Bank{
    void roi(){ System.out.println("CanaraBank Interest: "+b*0.08); }
}
class BankTest{
    public static void main(String[] a){
        Scanner s=new Scanner(System.in);
        Bank[] b={new City(),new SBI(),new Canara()};
        for(Bank x:b){ x.read(s); x.show(); x.roi(); System.out.println(); }
        s.close();
    }
}
