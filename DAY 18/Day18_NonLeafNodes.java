import java.util.*;

class Day18_NonLeafNodes {

    static class Node {
        int val;
        Node left, right;

        Node(int val) {
            this.val = val;
        }
    }

    static void nonLeaves(Node root, List<Integer> list) {
        if (root == null || (root.left == null && root.right == null))
            return;

        list.add(root.val);

        nonLeaves(root.left, list);
        nonLeaves(root.right, list);
    }

    public static void main(String[] args) {
        Node root = new Node(50);
        root.left = new Node(30);
        root.right = new Node(70);
        root.left.left = new Node(20);

        List<Integer> list = new ArrayList<>();
        nonLeaves(root, list);

        System.out.println(list);
    }
}