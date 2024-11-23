//3. (2p) Se citeste un numar n si o cifra c. Sa se insereze in n , inaintea fiecarei aparitii a cifrei c,
// cifra 9. Daca cifra c nu apare in numar , afisati „numar nemodificat”
//Exemplu: n=344594 si c=4 se afiseaza 394945994


import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n, c, rez=0, p=1;
        boolean cont = false;
        System.out.println("Enter your numbers: ");
        n = sc.nextInt();
        c = sc.nextInt();
        if (n==0 && c == 0){
            rez = 90;
            cont = true;
        }
        while (n > 0) {
            if (n % 10 == c) {
                rez = p * 10 * 9 + p * (n % 10) + rez;
                p *= 100;
                cont = true;
            } else {
                rez = p * (n % 10) + rez;
                p *= 10;
            }
            n /= 10;
        }
        if (cont)
            System.out.println(rez);
        else
            System.out.println("nu este modificat");

    }
}