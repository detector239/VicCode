#include <iostream>

using namespace std;

int main()
{
    double sales = 95000;
    cout << "Sales: $" << sales << endl;

    const double stateTaxRate = 0.04;
    double stateTax = sales * stateTaxRate;
    cout << "State Tax: $" << stateTax << endl;

    const double CountyTaxRate = 0.02;
    double countyTax = sales * CountyTaxRate;
    cout << "State Tax: $" << countyTax << endl;

    double totalTax = stateTax + countyTax;
    cout << "Total Tax: $" << totalTax << endl;

    return 0;
}
