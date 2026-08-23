class Day20_ArrayToBST {

    static class Node {
        int val;
        Node left, right;

        Node(int val) {
            this.val = val;
        }
    }

    static Node build(int[] arr, int low, int high) {

        if (low > high)
            return null;

        int mid = low + (high - low) / 2;

        Node root = new Node(arr[mid]);

        root.left = build(arr, low, mid - 1);
        root.right = build(arr, mid + 1, high);

        return root;
    }

    static void inorder(Node root) {

        if (root == null)
            return;

        inorder(root.left);

        System.out.print(root.val + " ");

        inorder(root.right);
    }

    public static void main(String[] args) {

        int[] arr = {10, 20, 30, 40, 50, 60, 70};

        Node root = build(arr, 0, arr.length - 1);

        inorder(root);
    }
}