#include <iostream>


int main()
{
    int number1 = 0b1111111; //0b is for binary form of numbers
    int number2 = 0xfa; //0x is for hexadecimal form of numbers
    int number3 = 037; //0 is for octal form of numbers
    int number4 = 255;
    std::cout << number1 << std::endl;
    std::cout << number2 << std::endl;
    std::cout << number3 << std::endl;
    std::cout << number4 << std::endl;

    std::cout << std::hex << number4 << std::endl;//we write like this if we want to print the hexadecimal form of the number that is in number4
    std::cout << std::oct << number4 << std::endl;//we write like this if we want to print the octadecimal form of the number that is in number4

    int num = 1'000'000; // the ' is there so it will be easier to read
    std::cout << num << std::endl;
    return 0;
}
