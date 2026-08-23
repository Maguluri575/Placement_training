import java.util.*;

class Day16_MinStack {
    public static void main(String[] args) {
        Stack<Integer> st = new Stack<>();
        Stack<Integer> min = new Stack<>();

        int[] a = {5, 2, 8, 1};

        for (int x : a) {
            st.push(x);

            if (min.isEmpty() || x <= min.peek())
                min.push(x);
        }

        System.out.println("Minimum: " + min.peek());
    }
}