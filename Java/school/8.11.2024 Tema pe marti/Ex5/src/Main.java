//  5.Se citeste un numar natural n cu cel mult 9 cifre. Sa se calculeze numarul obtinut din cifrele lui pare aflate
//  pe pozitii impare, numararea pozitiilor cifrelor incepand cu cifra cea mai semnificativa.(Cifra cea mai
//  semnificativa este prima cifra a numarului , deci numararea incepe de la stanga la dreapta, incepand de la 1)
//  Ex: daca n=2346561 rezulta 24

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        int n, m=0, c=1, i=0;
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter number: ");
        n = sc.nextInt();
        while (n>0){
            i = i*10+n%10;
            n /= 10;
        }
        while(i>0){
            if (i%2==0 && c%2==1){
                m = m*10 + i%10;
            }
            i = i/10;
            c++;
        }
        System.out.println(m);
    }
}