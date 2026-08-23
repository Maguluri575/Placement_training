class Day17_SlidingWindow {
    public static void main(String[] args) {
        int[] a = {1, 3, -1, -3, 5, 3, 6};
        int k = 3;

        for (int i = 0; i <= a.length - k; i++) {
            int max = a[i];

            for (int j = i; j < i + k; j++)
                max = Math.max(max, a[j]);

            System.out.print(max + " ");
        }
    }
}