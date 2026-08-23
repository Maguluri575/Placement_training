class Day11_FirstNonRepeating {

    public static void main(String[] args) {

        String s = "aabbcde";

        for (int i = 0; i < s.length(); i++) {

            char ch = s.charAt(i);
            int count = 0;

            for (int j = 0; j < s.length(); j++) {
                if (s.charAt(j) == ch)
                    count++;
            }

            if (count == 1) {
                System.out.println(ch);
                break;
            }
        }
    }
}