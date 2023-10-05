/*Write a program that reads a number, N, from standard input and computes the sum of the first N natural numbers (N included).
Sample input: 4
Sample output: 10*/

#include <iostream>

using namespace std;

int main()
{
    int num, res=0;

    cout << "You will enter a number and we will output the sum of all numbers smaller and equal to your number.\n";
    cout << "Your number:\n> ";
    cin >> num;

    for (int i = 1; i <= num; i++)
    {
        res = res + i;
    }

    cout <<"The result is "<< res;
    return 0;
}
