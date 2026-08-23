import java.util.Scanner;
import java.util.Arrays;

public class CompareTwoArrays {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter size of arrays: ");
        int n = sc.nextInt();

        int arr1[] = new int[n];
        int arr2[] = new int[n];

        System.out.println("Enter elements for Array 1:");
        for (int i = 0; i < n; i++) {
            arr1[i] = sc.nextInt();
        }

        System.out.println("Enter elements for Array 2:");
        for (int i = 0; i < n; i++) {
            arr2[i] = sc.nextInt();
        }

        Arrays.sort(arr1);
        Arrays.sort(arr2);

        int flag = 0;

        for (int i = 0; i < n; i++) {
            if (arr1[i] != arr2[i]) {
                flag = 1;
                break;
            }
        }

        if (flag == 0)
            System.out.println("Arrays are Same");
        else
            System.out.println("Arrays are Not Same");
    }
}