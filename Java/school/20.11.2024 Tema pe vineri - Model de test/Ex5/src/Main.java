//5. (1,5p)Se citesc mai multe numere naturale pana la 0. Determinati cel mai mare numar par citit.
//Daca nu s-a citit niciun numar par se afiseaza mesajul “nu exista”
//Exemplu: 2 3 8 4 5 7 9 8 3 0 se afiseaza 8

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n, max=-1;

        System.out.println("Enter your numbers: ");
        n = sc.nextInt();

        while(n!=0){
            if (n%2==0 && n>max) max = n;
            n = sc.nextInt();
        }
        if (max == -1) System.out.println("nu exista");
        else System.out.println(max);

    }
}