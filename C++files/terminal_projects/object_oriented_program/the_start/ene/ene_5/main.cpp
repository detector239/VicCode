/*5.  Write a program that finds the roots of a second degree equation. Considering the equation of the form
ax2+bx+c, the program will read a, b, and c from standard input. The program will output the two solutions for when the equation equals 0.
Sample input: 1  6  5
Sample output: -5.0   -1.0*/

#include <iostream>
#include <bits/stdc++.h>
#include <vector>
#include <string>
#include <cmath>

int main()
{
    std::vector<int> num_list{};
    std::vector<std::string> num_list_s{};
    std::string num_string;

    std::cout << ".\n";
    std::cout << "Write the numbers(delimit the numbers by space, but no space at the end):\n> ";

    std::getline(std::cin, num_string);
    std::string str, num = "";

    for (auto c : num_string)
    {
        str.push_back(c);
        num_list_s.push_back(str);
        str = "";
    }

    for (auto c : num_list_s)
    {
        if (!(c == " "))
        {
            str = c;
            num = num + str;
            str = "";
        }
        else
        {
            num_list.push_back(stoi(num));
            num = "";
        }
    }
    num_list.push_back(stoi(num));

    if (!(num_list.size() == 3))
    {
        std::cout << "You didn't input 3 numbers. \nQuitting...";
        exit(0);
    }

    auto a = num_list[0];
    auto b = num_list[1];
    auto c = num_list[2];

    double delta = sqrt(b*b-4*a*c);

    if (!(delta < 0))
    {
        double res1 =  (-b - delta)/2*a;
        double res2 =  (-b + delta)/2*a;
        std::cout << res1 <<" "<< res2;
    }
    else
    {
        std::cout<<"The equation has no result";
    }

    return 0;
}
