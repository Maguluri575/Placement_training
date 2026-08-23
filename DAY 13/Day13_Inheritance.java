class Day13_Inheritance {

    static class Animal {

        void eat() {
            System.out.println("Eating");
        }
    }

    static class Dog extends Animal {

        void bark() {
            System.out.println("Barking");
        }
    }

    public static void main(String[] args) {

        Dog d = new Dog();

        d.eat();
        d.bark();
    }
}