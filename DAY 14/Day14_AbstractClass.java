abstract class Day14_AbstractClass {

    abstract void sound();

    void eat() {
        System.out.println("Eating");
    }

    static class Dog extends Day14_AbstractClass {

        void sound() {
            System.out.println("Bark");
        }
    }

    public static void main(String[] args) {

        Dog d = new Dog();

        d.sound();
        d.eat();
    }
}