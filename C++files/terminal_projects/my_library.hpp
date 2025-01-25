#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

#ifndef HEADER_H
#define HEADER_H

namespace math
{
    double power2(double num)
    {
        return num*num;
    }
    double power3(double num)
    {
        return num*num*num;
    }

    template <typename tmpl>
    void swap(tmpl& a, tmpl& b)
    {
        tmpl temp = a;
        a = b;
        b = temp;
    }

}


namespace str
{
    void input_int(int& num, std::string otext)
    {
        while(num+1)
        {
            std::cout << otext;
            std::cin >> num;
            std::string ttext = "You didn't input a natural number. Try again.\n";
            if(std::cin.fail()) std::cout << ttext;
            else break;
        }
    }

    std::vector<std::string> split(std::string text, std::string delimiter)
    {
        std::vector<std::string> str_list;
        std::string s;
        for (char c : text)
        {
            s.push_back(c);
            if (!(s == delimiter)) str_list.push_back(s);
            s = "";
        }

        std::vector<std::string>::iterator iter;
        for (int i = 0; i < int(str_list.size()); i++)
        {
            if(std::find(str_list.begin(), str_list.end(), "")!=str_list.end())
            {
                iter = std::find(str_list.begin(), str_list.end(), "");
                auto position = iter - str_list.begin() - 1;
                str_list.erase(str_list.begin() + position);
            }
            else
            {
                break;
            }
        }

        return str_list;
    }
}
#endif
