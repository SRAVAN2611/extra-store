import java.util.*;
class StrCmp{
    static String r(int x){
        return x==0?"Both strings are equal":x>0?
               "First string is greater":"Second string is greater";
    }
    static String usrstrcmp(String a,String b){
        return r(a.compareTo(b));
    }
    static String usrstrcmp(String a,String b,int n){
        return r(a.substring(0,Math.min(n,a.length()))
                .compareTo(b.substring(0,Math.min(n,b.length()))));
    }
    public static void main(String[] args){
        Scanner s=new Scanner(System.in);
        System.out.print("a:"); String a=s.nextLine();
        System.out.print("b:"); String b=s.nextLine();
        System.out.print("char:"); int n=s.nextInt();
        System.out.println("\nfull cmp:"+usrstrcmp(a,b));
        System.out.println("\npar cmp:"+usrstrcmp(a,b,n));
        s.close();
    }
}
