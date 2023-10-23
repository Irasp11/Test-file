public class Exercise_3 {
    public static void main(String[] args) {
        int[] array = {2, 6, 9, 12, 7, 15};

        for (int number : array) {
            if (number % 3 == 0) {
                System.out.println(number);
            }
        }
    }
}