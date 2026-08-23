class Day18_MinMax {

    static class Node {
        int val;
        Node left, right;

        Node(int val) {
            this.val = val;
        }
    }

    static int min = Integer.MAX_VALUE;
    static int max = Integer.MIN_VALUE;

    static void find(Node root) {
        if (root == null)
            return;

        min = Math.min(min, root.val);
        max = Math.max(max, root.val);

        find(root.left);
        find(root.right);
    }

    public static void main(String[] args) {
        Node root = new Node(50);
        root.left = new Node(30);
        root.right = new Node(70);
        root.left.left = new Node(20);

        find(root);

        System.out.println("Min = " + min);
        System.out.println("Max = " + max);
    }
}