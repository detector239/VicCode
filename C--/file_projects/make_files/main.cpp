#include <iostream>
#include <stdio.h>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

int main()
{
    vector<string> names = {"Alex", "Dan", "Adam", "Anonymous"};
    string o_file = "../original_file.txt";

    std::ofstream writef (o_file);

    for(string name : names)
    {
        writef << name << "\n\n";
    }
    writef.close();

    return 0;
}
