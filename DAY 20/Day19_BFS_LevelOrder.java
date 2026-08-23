import java.util.*;

class Day19_BFS_LevelOrder {

    static class Node {
        int val;
        Node left, right;

        Node(int val) {
            this.val = val;
        }
    }

    static void bfs(Node root) {

        if (root == null)
            return;

        Queue<Node> q = new LinkedList<>();
        q.add(root);

        while (!q.isEmpty()) {

            int size = q.size();

            for (int i = 0; i < size; i++) {

                Node current = q.remove();

                System.out.print(current.val + " ");

                if (current.left != null)
                    q.add(current.left);

                if (current.right != null)
                    q.add(current.right);
            }

            System.out.println();
        }
    }

    public static void main(String[] args) {

        Node root = new Node(1);
        root.left = new Node(2);
        root.right = new Node(3);
        root.left.left = new Node(4);
        root.left.right = new Node(5);

        bfs(root);
    }
}