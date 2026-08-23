class Day19_BoundaryView {

    static class Node {
        int val;
        Node left, right;

        Node(int val) {
            this.val = val;
        }
    }

    static void boundary(Node root) {
        if (root == null) return;

        System.out.print(root.val + " ");
        left(root.left);
        leaves(root.left);
        leaves(root.right);
        right(root.right);
    }

    static void left(Node root) {
        if (root == null) return;

        if (root.left != null) {
            System.out.print(root.val + " ");
            left(root.left);
        } else if (root.right != null) {
            System.out.print(root.val + " ");
            left(root.right);
        }
    }

    static void leaves(Node root) {
        if (root == null) return;

        leaves(root.left);

        if (root.left == null && root.right == null)
            System.out.print(root.val + " ");

        leaves(root.right);
    }

    static void right(Node root) {
        if (root == null) return;

        if (root.right != null) {
            right(root.right);
            System.out.print(root.val + " ");
        } else if (root.left != null) {
            right(root.left);
            System.out.print(root.val + " ");
        }
    }

    public static void main(String[] args) {
        Node root = new Node(1);
        root.left = new Node(2);
        root.right = new Node(3);
        root.left.left = new Node(4);
        root.left.right = new Node(5);
        root.right.right = new Node(6);

        boundary(root);
    }
}