class Day18_CountNodes {

    static class Node {
        int val;
        Node left, right;

        Node(int val) {
            this.val = val;
        }
    }

    static int count(Node root) {
        if (root == null)
            return 0;

        return 1 + count(root.left) + count(root.right);
    }

    public static void main(String[] args) {
        Node root = new Node(50);
        root.left = new Node(30);
        root.right = new Node(70);
        root.left.left = new Node(20);

        System.out.println(count(root));
    }
}