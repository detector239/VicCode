//4. (2p)Se citeste un numar natural n. Sa se calculeze suma sufixelor care incep cu o cifra impara.
//        Exemplu:n=1234 se afiseaza 1268(explicatie: 34+1234=1268)

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n, p=1, s=0;
        System.out.print("Enter your number: ");
        n = sc.nextInt();

        while(n/p>0) p *= 10;

        while(p>1){
            if (n/(p/10) % 2 == 1){
                s = s + n%p;
            }
            p /= 10;
        }
        System.out.println(s);

    }
}