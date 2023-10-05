#include <iostream>
#include <cmath>

int main()
{
    std::cout << sqrt(25) /*square root (radical din 25) from cmath*/<< std::endl;
    std::cout << remainder(10, 3.25) << std::endl;// remainder is the same as 10%3 but in remainder we can use float numbers
    std::cout << fmax(10, 3) /*it will give us the highest number */<< std::endl;
    std::cout << fmin(10, 3) /*it will give us the lowest number */<< std::endl;
    std::cout << round(10.5) /*it will round the value */<< std::endl;
    return 0;
}
