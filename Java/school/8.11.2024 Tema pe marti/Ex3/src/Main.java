//  3.Se citeste un numar natural n. Sa se determine daca el are cifrele ordonate
//  crescator sau descrescator sau cifrele lui nu sunt ordonate.

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        int n, N, c=1, d=1;
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter the number: ");
        n = N = sc.nextInt();
        if (n<0) {
            n = N = (-1)*n;
        }
        while (n>0){
            if (n%10 <= (n%100)/10) {
                c = 0;
                break;
            }
            n = n/10;
        }
        while (N>9){

            if (N%10 >= (N%100)/10) {
                d = 0;
                break;
            }
            N = N/10;
        }
        if (c==1 && d==1){
            System.out.println("Numarul are doar o cifra.");
        }
        else{
            if (c==1) System.out.println("Sunt ordonate crescator.");
            else if (d==1) System.out.println("Sunt ordonate descrescator.");
            else System.out.println("Nu sunt ordonate.");
        }
    }
}