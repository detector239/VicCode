//1. Se citesc mai multe numere pana la citirea valorii 0. Calculati suma numerelor citite.

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n, s=0;
        System.out.print("Enter your number: ");
        n = sc.nextInt();

        while (n!=0){
            s += n;
            System.out.print("Enter your number: ");
            n = sc.nextInt();
        }
        System.out.println(s);
    }
}