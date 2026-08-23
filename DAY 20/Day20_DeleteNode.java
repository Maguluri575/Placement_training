class Day20_DeleteNode {

    static class Node {
        int val;
        Node left, right;

        Node(int val) {
            this.val = val;
        }
    }

    static Node delete(Node root, int key) {

        if (root == null)
            return null;

        if (key < root.val) {

            root.left = delete(root.left, key);

        } else if (key > root.val) {

            root.right = delete(root.right, key);

        } else {

            // No left child
            if (root.left == null)
                return root.right;

            // No right child
            if (root.right == null)
                return root.left;

            // Two children
            Node successor = getMin(root.right);

            root.val = successor.val;

            root.right =
                delete(root.right, successor.val);
        }

        return root;
    }

    static Node getMin(Node root) {

        while (root.left != null)
            root = root.left;

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

        Node root = new Node(50);

        root.left = new Node(30);
        root.right = new Node(70);

        root.left.left = new Node(20);
        root.left.right = new Node(40);

        root = delete(root, 30);

        inorder(root);
    }
}