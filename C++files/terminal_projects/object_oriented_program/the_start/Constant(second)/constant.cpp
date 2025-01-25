#include <iostream>

using namespace std;

int main()
{
    const double pi = 1.1111; //constant number
    double x = ++pi; // it's not posible because pi-constant
    cout << x << " " << pi;
    return 0;
}
