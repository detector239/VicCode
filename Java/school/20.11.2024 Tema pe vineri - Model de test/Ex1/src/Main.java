//1. (1p) Să se scrie un algoritm în care se citesc 2 numere naturale a și b .Verificati dacă prima cifră a
//numărului a este egală cu ultima cifră a numărului b (mesaj DA/NU).

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a, b, p=0;
        System.out.println("Enter your numbers: ");
        a = sc.nextInt();
        b = sc.nextInt();
        while (a>0) {
            p = a%10;
            a = a/10;
        }
        if (p == b%10) System.out.println("DA");
        else System.out.println("NU");


    }
}