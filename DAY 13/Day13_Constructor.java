class Day13_Constructor {

    String name;
    int age;

    Day13_Constructor(String name, int age) {
        this.name = name;
        this.age = age;
    }

    void display() {
        System.out.println(name + " " + age);
    }

    public static void main(String[] args) {

        Day13_Constructor s =
            new Day13_Constructor("Charan", 21);

        s.display();
    }
}
