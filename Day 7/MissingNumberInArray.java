import java.util.Scanner;

public class MissingNumberInArray {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter n: ");
        int n = sc.nextInt();

        int arr[] = new int[n];
        int actual = 0;

        System.out.println("Enter the elements:");
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
            actual += arr[i];
        }

        int expected = n * (n + 1) / 2;

        System.out.println("Missing Number = " + (expected - actual));
    }
}