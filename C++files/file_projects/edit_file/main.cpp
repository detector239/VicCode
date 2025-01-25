#include <iostream>
#include <stdio.h>
#include <fstream>
#include <string>

using namespace std;

int main()
{
    string o_file = "../original_file.txt";
    string t_file = "../temporary_file.txt";

    std::ifstream o_fread(o_file); // We read the file
    std::ofstream t_fwrite(t_file);

    string word;
    while(o_fread >> word)// this will get every word
    {
        if (word.find("Anonymous")+1)
        {
            word.replace(word.find("Anonymous"), 9, "We found it");
        }
        t_fwrite << word << "\n";
    }

    o_fread.close();
    t_fwrite.close();

    remove(o_file.c_str());
    rename(t_file.c_str(), o_file.c_str());

    return 0;
}
