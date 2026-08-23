import java.util.*;

class Day16_BalancedParentheses {
    public static void main(String[] args) {
        String s = "((()))";
        Stack<Character> st = new Stack<>();

        for (char c : s.toCharArray()) {
            if (c == '(')
                st.push(c);
            else if (c == ')') {
                if (st.isEmpty()) {
                    System.out.println("Not Balanced");
                    return;
                }
                st.pop();
            }
        }

        System.out.println(st.isEmpty() ? "Balanced" : "Not Balanced");
    }
}