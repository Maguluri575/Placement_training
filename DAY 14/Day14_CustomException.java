class Day14_CustomException {

    static class AgeException extends Exception {

        AgeException(String message) {
            super(message);
        }
    }

    static void checkAge(int age) throws AgeException {

        if (age < 18) {
            throw new AgeException("Not Eligible");
        }

        System.out.println("Eligible");
    }

    public static void main(String[] args) {

        try {
            checkAge(16);
        }
        catch (AgeException e) {
            System.out.println(e.getMessage());
        }
    }
}