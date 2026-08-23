class Day14_MultipleExceptions {

    public static void main(String[] args) {

        try {
            int[] arr = {10, 20, 30};

            System.out.println(arr[5]);
        }
        catch (ArithmeticException e) {
            System.out.println("Arithmetic Error");
        }
        catch (ArrayIndexOutOfBoundsException e) {
            System.out.println("Invalid Array Index");
        }
        catch (Exception e) {
            System.out.println("Some Error");
        }
    }
}