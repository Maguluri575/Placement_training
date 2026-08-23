class Day13_ClassObject {

    String name = "Charan";
    int age = 21;

    void display() {
        System.out.println(name);
        System.out.println(age);
    }

    public static void main(String[] args) {

        Day13_ClassObject obj = new Day13_ClassObject();

        obj.display();
    }
}