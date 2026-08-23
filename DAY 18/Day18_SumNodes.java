class Day18_SumNodes {

    static class Node {
        int val;
        Node left, right;

        Node(int val) {
            this.val = val;
        }
    }

    static int sum(Node root) {
        if (root == null)
            return 0;

        return root.val + sum(root.left) + sum(root.right);
    }

    public static void main(String[] args) {
        Node root = new Node(50);
        root.left = new Node(30);
        root.right = new Node(70);

        System.out.println("Sum = " + sum(root));
    }
}