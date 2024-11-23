//8.Scrieți un program care citește un număr natural nenul n și care calculează suma tuturor numerelor
// sufixe pentru n.

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n, s=0, p=1;

        System.out.print("Enter your number: ");
        n = sc.nextInt();

        while (n>0){
            s += n/p;
            p *= 10;
            n /= 10;
        }
        System.out.println(s);
    }
}