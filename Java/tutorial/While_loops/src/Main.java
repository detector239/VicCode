import java.util.Locale;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String input = "";
        while (true) {
            System.out.print("Input: ");
            input = sc.nextLine().toLowerCase();
            if (input.equals("pass")) {
                continue;
            }
            if (input.equals("quit")) {
                break;
            }
            System.out.println(input);
        }
    }
}