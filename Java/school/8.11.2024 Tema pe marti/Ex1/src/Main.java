//  1.Se citeste un numar natural n. Calculati si afisati rasturnatul (oglinditul)
// sumei cifrelor lui n.
//  Exemplu: Pentru n=34565 se va afisa 32 (suma cifrelor este 23, iar
// rasturnatul lui 23 este 32).

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        int n, s=0, i=0;

        Scanner sc = new Scanner(System.in);
        System.out.print("Enter number: ");
        n = sc.nextInt();

        while (n>0){
            s = s + n%10;
            n = n/10;
        }
        while (s>0){
            i = i*10 + s%10;
            s = s/10;
        }
        System.out.println(i);
    }
}