// Write a program that reads an integer number from standard input and computes the sum of its digits.

#include <iostream>
#include <string>

using namespace std;

int main()
{
    std::string num_str;
    int res = 0;

    std::cout << "We will give you the sum of the digits from your number.\nYour number: ";
    std::cin >> num_str;

    for (auto digit : num_str)
    {
        std::string str(1, digit);
        res = res + stoi(str);
    }

    std::cout << "The result is " << res;
    return 0;
}
