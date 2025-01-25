/*Write a program that reads a string from standard input and prints each character in the string,
except spaces, using the for instruction. */

#include <iostream>
#include <bits/stdc++.h>
#include <vector>
#include <string>

using namespace std;

int main()
{
    vector<string> str_list;
    string str, s;

    getline(cin, str);

    for (char c : str)
    {
        s.push_back(c);
        if (!(s == " ")) str_list.push_back(s);
        s = "";
    }

    for (auto el : str_list)
    {
        cout << el + "\n";
    }
    return 0;
}
