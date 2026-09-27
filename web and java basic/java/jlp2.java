import java.util.*;
class jlp2{
public static void main(String[] a){
Scanner s=new Scanner(System.in);
System.out.print("n: ");int n=s.nextInt();
System.out.println("Enter: Name Id Dept Desg Age Salary");
String[] n1=new String[n],d=new String[n],g=new String[n];
int[] id=new int[n],age=new int[n]; double[] sal=new double[n];
for(int i=0;i<n;i++){
n1[i]=s.next(); id[i]=s.nextInt();
d[i]=s.next(); g[i]=s.next();
age[i]=s.nextInt(); sal[i]=s.nextDouble();
}
System.out.println("Details:\nName Id Dept Desg Age Salary");
for(int i=0;i<n;i++)
System.out.println(n1[i]+" "+id[i]+" "+d[i]+" "+g[i]+" "+age[i]+" "+sal[i]);
double sum=0,max=0; int k=0;
for(int i=0;i<n;i++){
if(d[i].equals("sales")) sum+=sal[i];
if(d[i].equals("purchase")&&g[i].equals("manager")&&sal[i]>max){max=sal[i];k=i;}
}
System.out.println("sum: "+sum);
System.out.println("high: "+n1[k]+" "+sal[k]);
s.close();
}}
