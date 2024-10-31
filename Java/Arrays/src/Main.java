import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        int[] numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
        numbers[0] = 7;
        System.out.println(Arrays.toString(numbers));

        int[][] num = new int[2][3];// two dimensional array
        num[0][2] = 7;
        System.out.println(Arrays.toString(num[0])); // we can't transform to string a multi dimensional arary
        // (we can but the output is not readble)
    }
}