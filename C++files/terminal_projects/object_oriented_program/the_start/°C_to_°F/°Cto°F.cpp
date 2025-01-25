#include <iostream>

using namespace std;

int main()
{
    double celsius;
    cout << "How much celsius do you want to convert?" <<endl;
    cout << "> ";
    cin >> celsius;
    cout << endl;
    double fahrenheit = (celsius * 1.8) + 32;
    cout << celsius << " Celsius are " << fahrenheit << " Fahrenheit." << endl;
    return 0;
}
