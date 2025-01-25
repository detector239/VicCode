/*Write a program that reads a number from the input and checks if the number is even.
If true, then the program prints "EVEN", otherwise it prints "ODD".*/

#include <iostream>

using namespace std;

double user_input()
{
    int num;
    cin >> num;
    if (cin.fail())
    {
        cout << "You didn't input a number. \nQuitting...";
        exit(0);
    }
    return num;
}

int main()
{
    int a, c;
    cout << "We will check if your number is even or odd.\n";
    cout << "Write your number: ";
    a = user_input();
    c = a%2;
    cout << a <<endl<<c<< endl;
    if (c == 0)
    {
        cout << "EVEN";
    }
    else
    {
        cout << "ODD";
    }
    return 0;
}
