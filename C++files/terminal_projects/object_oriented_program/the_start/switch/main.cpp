#include <iostream>


int main()
{
    enum class Seasons{winter, spring, summer, fall};
    Seasons now = Seasons::spring;
    switch(now)
    {
    case Seasons::winter:
        std::cout << "Now is winter!\n";
        break;
    case Seasons::spring:
        std::cout << "Now is spring!\n";
        break;
    case Seasons::summer:
        std::cout << "Now is summer!\n";
        break;
    case Seasons::fall:
        std::cout << "Now is fall!\n";
        break;
    }
    return 0;
}
