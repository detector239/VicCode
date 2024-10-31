
public class Main {
    public static void main(String[] args) {
        // Casting
        // byte > short > int > long > float > double
        double x = 1.9;
        int y = (int)x + 2;
        System.out.println(y);

        String z = "4";
        y = Integer.parseInt(z) + 5;
        System.out.println(y);
    }
}