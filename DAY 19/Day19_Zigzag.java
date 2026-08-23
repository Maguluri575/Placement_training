import java.util.*;

class Day19_Zigzag {

    static class Node {
        int val;
        Node left, right;

        Node(int val) {
            this.val = val;
        }
    }

    static void zigzag(Node root) {
        if (root == null) return;

        Queue<Node> q = new LinkedList<>();
        q.add(root);

        boolean leftToRight = true;

        while (!q.isEmpty()) {
            int n = q.size();
            int[] level = new int[n];

            for (int i = 0; i < n; i++) {
                Node temp = q.poll();

                int index = leftToRight ? i : n - 1 - i;
                level[index] = temp.val;

                if (temp.left != null) q.add(temp.left);
                if (temp.right != null) q.add(temp.right);
            }

            for (int x : level)
                System.out.print(x + " ");

            leftToRight = !leftToRight;
        }
    }

    public static void main(String[] args) {
        Node root = new Node(1);
        root.left = new Node(2);
        root.right = new Node(3);
        root.left.left = new Node(4);
        root.right.right = new Node(5);

        zigzag(root);
    }
}