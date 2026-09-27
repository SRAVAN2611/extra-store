import java.util.*;
class P{String n,g;int a;P(String n,int a,String g){this.n=n;this.a=a;this.g=g;}}
class E extends P{String d;E(String n,int a,String g,String d){super(n,a,g);this.d=d;}
void show(){System.out.println(n+" "+a+" "+g+" "+d);}}
class S extends P{String c;S(String n,int a,String g,String c){super(n,a,g);this.c=c;}
void show(){System.out.println(n+" "+a+" "+g+" "+c);}}
class jlp4{
public static void main(String[] x){
Scanner s=new Scanner(System.in);
E[] e=new E[5];S[] st=new S[5];
System.out.println("Emp (name age gender designtion):");
for(int i=0;i<5;i++)e[i]=new E(s.next(),s.nextInt(),s.next(),s.next());
System.out.println("Stu (name age gender course):");
for(int i=0;i<5;i++)st[i]=new S(s.next(),s.nextInt(),s.next(),s.next());
System.out.println("\nEmployee Details:");
System.out.println("Emp (name age gender designtion):");
for(E i:e)i.show();
System.out.println("\nStudent Details:");
System.out.println("Stu (name age gender course):");
for(S i:st)i.show();
s.close();
}}
