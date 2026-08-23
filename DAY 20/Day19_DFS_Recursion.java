class Day19_DFS_Recursion {

    static class Node {
        int val;
        Node left, right;

        Node(int val) {
            this.val = val;
        }
    }

    static void dfs(Node root) {

        if (root == null)
            return;

        System.out.print(root.val + " ");

        dfs(root.left);
        dfs(root.right);
    }

    public static void main(String[] args) {

        Node root = new Node(1);
        root.left = new Node(2);
        root.right = new Node(3);
        root.left.left = new Node(4);
        root.left.right = new Node(5);

        dfs(root);
    }
}