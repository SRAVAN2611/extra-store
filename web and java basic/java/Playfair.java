import java.util.*;
class Playfair {
    public static void main(String[] z) {
        Scanner x = new Scanner(System.in);
        System.out.print("key: ");
        String s = "", k = x.nextLine().toUpperCase() + "ABCDEFGHIKLMNOPQRSTUVWXYZ";
        for (char c : k.toCharArray()) if (s.indexOf(c = c == 'J' ? 'I' : c) < 0) s += c;
        System.out.println("matrix:");
        for (int i = 0; i < 25; i++) System.out.print(s.charAt(i) + (i % 5 == 4 ? "\n" : " "));
        System.out.print("pt: ");
         String q = x.nextLine().toUpperCase().replaceAll("[^A-Z]", "").replace("J", "I");
        String p = "";
        for (int i = 0; i < q.length(); )
            if (i + 1 < q.length() && q.charAt(i) == q.charAt(i + 1))
                p += q.charAt(i++) + "X";
            else
                p += "" + q.charAt(i++) + (i < q.length() ? q.charAt(i++) : 'X');
        System.out.print("ct: ");
        for (int i = 0; i < p.length(); i += 2) {
            int a = s.indexOf(p.charAt(i)), b = s.indexOf(p.charAt(i + 1)), r1 = a / 5, c1 = a % 5, r2 = b / 5, c2 = b % 5;
            System.out.print("" + s.charAt(r1 == r2 ? r1 * 5 + (c1 + 1) % 5 : c1 == c2 ? (r1 + 1) % 5 * 5 + c1 : r1 * 5 + c2) + s.charAt(r1 == r2 ? r2 * 5 + (c2 + 1) % 5 : c1 == c2 ? (r2 + 1) % 5 * 5 + c2 : r2 * 5 + c1));
        }
        x.close();
    }
}