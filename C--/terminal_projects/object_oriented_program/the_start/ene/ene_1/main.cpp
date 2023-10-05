/* Write a program that reads two numbers, a,b, and outputs the one which is greater.
If the numbers are equal, then the program should print the message "the numbers are equal". */


#include <iostream>

using namespace std;

void user_input(auto num)
{

    cin >> num;
    if (cin.fail())
    {
        cout << "You didn't input a number. \nQuitting...";
        exit(0);
    }
}
int main()
{
    int a, b;
    cout << "You will write 2 numbers and I will compare them\n";
    cout << "Write the first number a: ";
    user_input(a);
    cout << "Write the first number b: ";
    user_input(b);

    if(a > b)
    {
        cout << "a is greater than b";
    }
    else if(a < b)
    {
        cout << "b is greater than a";
    }
    else
    {
        cout << "the numbers are equal";
    }
    return 0;
}
