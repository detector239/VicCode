public class Main {
    public static void main(String[] args) {
        // Comparison operators: >, >=, <, <=, ==, !=
        // Logical operators: &&, ||, !
        int temp = 22;
        boolean isWarm = temp > 20 && temp < 27;
        System.out.println(isWarm);

        boolean hasHighIncome = true;
        boolean hasGoodCredit = true;
        boolean hasCriminalRecords = false;
        boolean isElilgible = (hasHighIncome || hasGoodCredit) && !hasCriminalRecords;
        System.out.println(isElilgible);

    }
}