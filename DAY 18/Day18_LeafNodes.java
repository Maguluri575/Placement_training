import java.util.*;

class Day18_LeafNodes {

    static class Node {
        int val;
        Node left, right;

        Node(int val) {
            this.val = val;
        }
    }

    static void leaves(Node root, List<Integer> list) {
        if (root == null)
            return;

        if (root.left == null && root.right == null) {
            list.add(root.val);
            return;
        }

        leaves(root.left, list);
        leaves(root.right, list);
    }

    public static void main(String[] args) {
        Node root = new Node(50);
        root.left = new Node(30);
        root.right = new Node(70);
        root.left.left = new Node(20);
        root.left.right = new Node(40);

        List<Integer> list = new ArrayList<>();
        leaves(root, list);

        System.out.println(list);
    }
}