// calculate factorial

#include <iostream>

using namespace std;

int main()
{
    int factorial = 7, i = factorial-1;

    while(i > 1)
    {
        factorial *= i;
        i--;
    }
    cout << factorial << endl;
}
