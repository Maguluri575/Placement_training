class Day20_KthSmallest {

    static class Node {
        int val;
        Node left, right;

        Node(int val) {
            this.val = val;
        }
    }

    static int count = 0;

    static int kthSmallest(Node root, int k) {

        if (root == null)
            return -1;

        int left = kthSmallest(root.left, k);

        if (left != -1)
            return left;

        count++;

        if (count == k)
            return root.val;

        return kthSmallest(root.right, k);
    }

    public static void main(String[] args) {

        Node root = new Node(50);

        root.left = new Node(30);
        root.right = new Node(70);

        root.left.left = new Node(20);
        root.left.right = new Node(40);

        count = 0;

        int k = 3;

        System.out.println("Kth Smallest: "
                + kthSmallest(root, k));
    }
}