#include <iostream>


int main()
{
    double num1, num2, result;
    char operation_str;

    std::cout << "the first number: ";
    std::cin >> num1;

    std::cout << "the second number: ";
    std::cin >> num2;

    std::cout << "the operation: ";
    std::cin >> operation_str;
    int operation = int(operation_str);
    switch(operation)
    {
    case 43:
        result = num1 + num2;
        std::cout << "The result is: " << result;
        break;
    case 45:
        result = num1 - num2;
        std::cout << "The result is: " << result;
        break;
    case 42:
        result = num1 * num2;
        std::cout << "The result is: " << result;
        break;
    case 47:
        result = num1 / num2;
        std::cout << "The result is: " << result;
        break;
    default:
        std::cout << "Something went wrong. Quitting...";
        break;
    }
    return 0;
}
