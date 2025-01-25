#include <iostream>
#include <cstring>
#include "./header.h"
#include "../my_library.cpp"

double input_int(std::string text);

int main()
{
    int a=20, b;
    input_int("Enter any number;\n>");
    swap(a, b);
    std::cout << "a = " << a << "\nb = " << b << std::endl;

    std::string name1 = "Popovici";
    std::string name2 = "Cioban";

    swap(name1, name2);
    std::cout << "name1 = " << name1 << "\nname2 = " << name2 << std::endl;
    return 0;
}
