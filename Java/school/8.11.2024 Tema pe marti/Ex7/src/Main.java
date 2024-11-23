//7. Scrieți un program care citește un număr natural nenul n și care calculează suma tuturor
// numerelor prefixe pentru n.

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n, s=0;
        System.out.print("Enter your number: ");
        n = sc.nextInt();
        while (n>0){
            s += n;
            n /= 10;
        }
        System.out.println(s);
    }
}