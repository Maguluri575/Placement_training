class Day14_Encapsulation {

    private int marks;

    void setMarks(int marks) {
        this.marks = marks;
    }

    int getMarks() {
        return marks;
    }

    public static void main(String[] args) {

        Day14_Encapsulation s = new Day14_Encapsulation();

        s.setMarks(90);

        System.out.println(s.getMarks());
    }
}
