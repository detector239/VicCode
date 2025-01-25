#include <iostream>
#include <math.h>


double pow(double base, int exponent){
    double result = 1;
    for(int i=1; i<=exponent; i++){
        result = result * base;
    }
}

void print_pow(int base, int exponent){
    double myPower = pow(base, exponent);
    std::cout << base << " raised to the " << exponent << " power is "<< myPower << ".\n";
}
int main()
{
    double base;
    int exponent;
    std::cout << "What is the base?\n> ";
    std::cin >> base ;
    std::cout << "What is the exponent?\n> ";
    std::cin >> exponent ;
    print_pow(base, exponent);
    return 0;
}
