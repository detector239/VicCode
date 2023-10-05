#include <iostream>
#include "../my_library.hpp"

using namespace std;

int main()
{
    int num1, num2;
    std::string text1 = "Input any number:\n ";
    std::string text2 = "Input again any number:\n> ";

    str::input_int(num1, text1);
    str::input_int(num2, text2);

    num1 = int(math::power2(num1));
    num2 = int(math::power3(num2));

    std::cout << "Before swap:\n";
    std::cout << "num1 = " << num1 << std::endl;
    std::cout << "num2 = " << num2 << std::endl;

    math::swap(num1, num2);

    std::cout << "After swap:\n";
    std::cout << "num1 = " << num1 << std::endl;
    std::cout << "num2 = " << num2 << std::endl;

    std::cout << "\nInput any text:\n";

    std::string line;
    std::getline(std::cin, line);

    std::vector<std::string> vec = str::split(line, " ");
    for (int i = 0; i<int(vec.size()); i++)
    {
        std::cout << vec[i] << "  ";
    }
    return 0;
}
