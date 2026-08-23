import java.util.*;

class Day16_NextGreater {
    public static void main(String[] args) {
        int[] a = {4, 5, 2, 10};
        Stack<Integer> st = new Stack<>();

        for (int i = a.length - 1; i >= 0; i--) {
            while (!st.isEmpty() && st.peek() <= a[i])
                st.pop();

            System.out.print((st.isEmpty() ? -1 : st.peek()) + " ");
            st.push(a[i]);
        }
    }
}