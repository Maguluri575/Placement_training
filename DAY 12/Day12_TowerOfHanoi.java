class Day12_TowerOfHanoi {

    static void hanoi(int n, char source, char helper, char destination) {

        if (n == 0)
            return;

        hanoi(n - 1, source, destination, helper);

        System.out.println(source + " -> " + destination);

        hanoi(n - 1, helper, source, destination);
    }

    public static void main(String[] args) {

        hanoi(3, 'A', 'B', 'C');
    }
}
