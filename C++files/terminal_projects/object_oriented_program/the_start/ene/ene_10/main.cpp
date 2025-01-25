//Write a program that reads an integer, N, and outputs all even numbers less than N, including N if its even.


#include <iostream>

using namespace std;

int main()
{
    int num;

    cout << "You wll write any natural number and we will output all even numbers less than your number\nYour number:\n> ";
    cin >> num;

    for (int i = 1; i<=num; i++) if (i%2 == 0) cout << i << endl;
    return 0;
}
