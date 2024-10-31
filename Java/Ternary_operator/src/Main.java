public class Main {
    public static void main(String[] args) {
        int income = 120_000;
        String className = income > 100_000 ? "First" : "Economy";
        System.out.println(className);
        // The same as
        // if (income > 100_000) className = "First";
        // else className = "Economy";
    }
}