import java.util.*;

public class p1 {
  static String c(String t, int s) {
    var b = new StringBuilder();
    for (char ch : t.toCharArray())
      b.append(Character.isLetter(ch) ?
        (char)((ch - (Character.isUpperCase(ch) ? 'A' : 'a') + s) % 26 + (Character.isUpperCase(ch) ? 'A' : 'a')) : ch);
    return b.toString();
  }

  public static void main(String[] a) {
    var s = new Scanner(System.in);
    System.out.print("Message: ");
    var m = s.nextLine();
    System.out.print("Shift: ");
    var sh = s.nextInt();
    System.out.println("Encrypted: " + c(m, sh));
    System.out.println("Decrypted: " + c(c(m, sh), 26 - sh));
    s.close();
  }
}