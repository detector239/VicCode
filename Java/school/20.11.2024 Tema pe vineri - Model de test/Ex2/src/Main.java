//2. (1,5p)Se citeste un numar a . Sa se verifice dacă numărul a este de forma xyyyyyyy (prima cifră diferita
// de toate celelalte, celelalte toate egale)
//Exemplu: n=12222 se afiseaza „da”

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a, p=1, pc, u=0;
        boolean c = true;
        System.out.print("Enter your number: ");
        a = sc.nextInt();

        if (a != 0) {
            while (a / p != 0) p *= 10;
        }
        else p = 10;

        pc = a / (p / 10);
        u = a % 10;
        a = a % (p/10);

        while (a>0){
            if (u != a%10){
                c = false;
            }
            u = a%10;
            a = a/10;
        }

        if (c && pc!=u) System.out.println("da");
        else System.out.println("nu");


    }
}