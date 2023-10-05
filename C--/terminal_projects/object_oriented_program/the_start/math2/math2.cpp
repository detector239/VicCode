#include <iostream>

using namespace std;

int main()
{
    double x = 10;
    double y = 5;
    double z = (x + 10)/(3*y); // z = 1.3
    cout << z << endl;
    z = (x + 10)/3*y; // z = 33.3, because z = [(x+10)/3]*y
    cout << z << endl;
    int a = 10;

    int b = a++; // b = a(10), a = a+1(11)
    cout << b << " " << a << endl;
    b = ++a; // b = a+1(12), a = a+1(12)
    cout << b << " " << a << endl;
    return 0;
}
