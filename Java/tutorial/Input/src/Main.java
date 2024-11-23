import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter name: ");
        String name = sc.nextLine().trim(); // "trim()" removes the spaces before and after the string
        // we  can also use .nextByte() or .nextInt() and others
        System.out.println("Your name is " + name);
    }
}