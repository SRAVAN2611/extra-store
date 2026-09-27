import javax.crypto.*;import javax.crypto.spec.*;import java.security.*;import java.util.*;
public class mix3{
    public static void main(String[] a) throws Exception{
        Scanner s=new Scanner(System.in);
        //String ALG="DES";
        //String ALG="AES";
        String ALG="RSA";
        System.out.print("message: ");String m=s.nextLine();
        if(ALG=="RSA"){
            Cipher c=Cipher.getInstance("RSA");
            KeyPair kp= KeyPairGenerator.getInstance("RSA").generateKeyPair();
            c.init(Cipher.ENCRYPT_MODE,kp.getPublic());byte[] e=c.doFinal(m.getBytes());
            System.out.println("enc: "+Base64.getEncoder().encodeToString(e));
            c.init(Cipher.DECRYPT_MODE,kp.getPrivate());
            System.out.println("dec: "+new String(c.doFinal(e)));
        } else{
            System.out.print(ALG=="DES"?"Password(8 chars): ":"Key(16 chars): ");
            SecretKey k=new SecretKeySpec(s.nextLine().getBytes(),ALG);
            Cipher c=Cipher.getInstance(ALG);
            c.init(Cipher.ENCRYPT_MODE,k);byte[] e=c.doFinal(m.getBytes());
            System.out.println("enc: "+Base64.getEncoder().encodeToString(e));
            c.init(Cipher.DECRYPT_MODE,k);
            System.out.println("dec: "+new String(c.doFinal(e)));
        }
        s.close();
    }
}