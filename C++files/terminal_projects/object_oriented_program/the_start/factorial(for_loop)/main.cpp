#include <iostream>

int main()
{
    // start example
    int i;
    for(i = 9; i >= 0; i--)// this will count down till 0
    {
        std::cout << i << std::endl;
    }
    std::cout << std::endl;
    for(i = 0; i < 10; i++)
    {
        std::cout<< i << std::endl;
    }
    // finish example
    // start factorial program
    long long factorial;
    std::cout << "We will calculate the factorial for the number that you will input.\nThe number: ";
    std::cin >> factorial;
    short fact_num = factorial;
    if(factorial > 0)
    {
        for(i = factorial - 1; i > 0; i--)
        {
            factorial = factorial * i;
        }
        std::cout << "The factorial of the number " << fact_num << " is " << factorial << std::endl;
    }
    else
    {
        std::cout << "Something went wrong. Quitting...";
    }
    return 0;
}
