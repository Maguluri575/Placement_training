class Day17_CircularQueue {
    public static void main(String[] args) {
        int[] q = new int[5];
        int rear = 0;

        q[rear] = 10;
        rear = (rear + 1) % 5;

        q[rear] = 20;
        rear = (rear + 1) % 5;

        q[rear] = 30;

        for (int x : q)
            System.out.print(x + " ");
    }
}