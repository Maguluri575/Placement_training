import java.util.Scanner;

public class CountCharacters {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter a String: ");
        String s = sc.nextLine();

        int upper = 0, lower = 0, number = 0, space = 0, symbol = 0;

        for (int i = 0; i < s.length(); i++) {

            char ch = s.charAt(i);

            if (Character.isUpperCase(ch))
                upper++;
            else if (Character.isLowerCase(ch))
                lower++;
            else if (Character.isDigit(ch))
                number++;
            else if (ch == ' ')
                space++;
            else
                symbol++;
        }

        System.out.println("Capital Letters : " + upper);
        System.out.println("Small Letters   : " + lower);
        System.out.println("Numbers         : " + number);
        System.out.println("Spaces          : " + space);
        System.out.println("Symbols         : " + symbol);
    }
}