/*Write the program that outputs the maximum out of 3 numbers read from standard input.
Sample input: 2 4 1
Sample output: 4*/

#include <iostream>
#include <bits/stdc++.h>
#include <vector>
#include <string.h>
#include <cstring>

int main()
{
    std::vector<std::string> num_list_s{};
    std::vector<int> num_list{};
    std::string num_string;

    std::cout << "You will write a list of numbers and we will print the biggest number\n";
    std::cout << "Write the list of numbers(only natural numbers divided by 1 space, no space at the end):\n> ";
    std::getline(std::cin, num_string);
//                                          23  45
    std::string str;
    for (auto c : num_string)
    {
        str.push_back(c);
        num_list_s.push_back(str);
        str = "";
    }

    string::

    std::string num;
    for (auto c : num_list_s)
    {
        if (!(c == " "))
        {
            if (!(std::isdigit(*(num.c_str()))))
            {
                num = "";
            }
            str = c;
            num = num + str;
            str = "";
        }
        else
        {
            num_list.push_back(stoi(num));
            num = "null";
        }
    }
    num_list.push_back(stoi(num));

    int list_size = int(num_list.size());
    auto result = num_list.at(0);
    for (int c = 0; !(c == list_size); ++c)
    {
        auto num = num_list.at(c);
        if (result < num)
        {
            result = num;
        }
    }
    std::cout << result;
    return 0;
}
