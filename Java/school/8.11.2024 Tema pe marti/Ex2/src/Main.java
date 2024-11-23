//2.Se citeste un numar natural n. Afisati cele 2 numere obtinute prin impartirea "la mijloc"a numarului n.
// Exemple: n=12345 se afiseaza 12 si 345
//        n= 12345678 se afiseaza 1234 5678

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        int n, N, c=0, p;
        Scanner sc =  new Scanner(System.in);
        System.out.print("Enter number: ");
        n = N = sc.nextInt();

        while (n>0){
            c++;
            n = n/10;
        }
        c = c%2==1 ? c/2+1 : c/2;
        p = 1;
        while (c>-1){
            p *= 10;
            c--;
        }
        p = p/10;
        System.out.println(N/p + " " + N%p);
    }
}

