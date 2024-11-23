//6. Două numere sunt “bune” dacă cifra maximă a unui număr coincide cu cifra minimă din celălalt sau invers.
// Se dau două numere a și b numere naturale. Verificați dacă cele două numere sunt “bune” și afișați cifra comună.
// Dacă cele două numere nu sunt bune, afișați NU.
//Exemplu: daca cele doua numere sunt 123 3456 se afiseaza 3

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a, b, min1=9, min2=9, max1=0, max2=0;
        System.out.println("Enter 2 numbers: ");
        a = sc.nextInt();
        b = sc.nextInt();
        while (a > 0){
            min1 = Math.min(min1, a%10);
            max1 = Math.max(max1, a%10);
            a = a/10;
        }
        while (b > 0){
            min2 = Math.min(min2, b%10);
            max2 = Math.max(max2, b%10);
            b = b/10;
        }
        if (min1 == max2 || min2==max1) System.out.println("sunt bune");
        else System.out.println("nu sunt bune");
    }
}