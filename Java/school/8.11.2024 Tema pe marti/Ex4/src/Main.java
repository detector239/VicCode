//4. Se citesc 2 numere naturale a si b. Sa se determine cate cifre egale se afla pe pozitii indentice
// in cele doua numere.
//        Exemplu:
//a=3421345
//b=4531125
//cifre egale pe pozitii identice sunt cifra unitatilor si cea a miilor, deci doua.

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        int a, b, c=0;
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter two numbers: ");
        a = sc.nextInt();
        b = sc.nextInt();

        if (a==0 && b==0) System.out.println(1);
        else if ((a==0 || b==0) && (a==b%10 || b==a%10))
            System.out.println(1);
        else {
            while (!(a == 0 || b == 0)) {
                if (a % 10 == b % 10) c++;
                a = a / 10;
                b = b / 10;
            }
            System.out.println(c);
        }
    }
}