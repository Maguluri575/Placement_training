class Day19_LCA {

    static class Node {
        int val;
        Node left, right;

        Node(int val) {
            this.val = val;
        }
    }

    static Node lca(Node root, int a, int b) {
        if (root == null)
            return null;

        if (a < root.val && b < root.val)
            return lca(root.left, a, b);

        if (a > root.val && b > root.val)
            return lca(root.right, a, b);

        return root;
    }

    public static void main(String[] args) {
        Node root = new Node(50);
        root.left = new Node(30);
        root.right = new Node(70);
        root.left.left = new Node(20);
        root.left.right = new Node(40);

        Node ans = lca(root, 20, 40);

        System.out.println(ans.val);
    }
}