/*Write a program that computes your grade for the Programming course:
lab_grade = (test_1 + test_2)/2
final_grade = 70% lab_grade + 30% exam_grade
The input consists of three grades, for the first test, for the second test, and for the exam.
If any of the lab grade or the exam grade are less than 5 the program will print: "failed". Otherwise, the program will print the final grade.
Sample input: 4 10 8
Sample output: 7.3*/

#include <iostream>
#include <bits/stdc++.h>
#include <vector>
#include <string>


int main()
{
    std::vector<int> num_list{};
    std::vector<std::string> num_list_s{};
    std::string num_string;

    std::cout << "You will write a list of numbers and we will find the average.\n";
    std::cout << "Write a list of numbers(delimit the numbers by space, but no space at the end):\n> ";
    std::getline(std::cin, num_string);
//                                             23  45
    std::string num, str;
    int a=0, b;

    for (b = 0; b <= num_string.size(); b++)
    {
        b = num_string.find(" ");
        if (num_string.at(b) == num_string.at(b+1)) num_string.erase(b);
        b = b+1;
    }
    b = 0;
    for (char ch : num_string+" ")
    {
        if (ch == ' ')
        {
            b = num_string.find(ch, a+1);
            num = num_string.substr(a, b);
            std::cout << num;
            if (!(num == "") || !(num == " "))
            {
                num_list.push_back(stoi(num));
            }
            num_string.erase(num_string.begin(), num_string.begin()+b+1);
            b = 0;
            num = "";
        }
    }
    for (auto el : num_list)
    {
        std::cout << el << std::endl;
    }



//                                          23 56
    /*std::string str, num = "";
    for (auto c : num_string)
    {
        str.push_back(c);
        num_list_s.push_back(str);
        str = "";
    }

    for (auto c : num_list_s)
    {
        //std::cout << c << std::endl;
        if (!(c == " "))
        {
            str = c;
            num = num + str;
            str = "";
        }
        else
        {
            //std::cout << num << ".";
            num_list.push_back(stoi(num));
            num = "";
        }
    }
    num_list.push_back(stoi(num));*/

    double result;
    for (auto el : num_list)
    {
        result = result + el;
    }
    std::cout <<"The average is: "<< result/num_list.size();
    return 0;
}
