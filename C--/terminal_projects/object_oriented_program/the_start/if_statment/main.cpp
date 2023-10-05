#include <iostream>


int main()
{
    int age;
    std::cout << "What is your age?: ";
    std::cin >> age;
    if(age <= 13)
    {
        std::cout << "You're not old enough\n";
    }
    else if(age < 19)
    {
        std::cout << "You're almost 19\n";
    }
    else
    {
        std::cout << "You can go\n";
    }
    return 0;
}
