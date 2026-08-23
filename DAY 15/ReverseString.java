import java.util.Scanner;

public class ReverseString {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter a String: ");
        String s = sc.next();

        int i = s.length();

        while (i > 0) {
            System.out.print(s.charAt(i - 1));
            i--;
        }
    }
}