#include <iostream>
#include <fstream>
#include <string>


using namespace std;

int main()
{
    string file_name = "../original_file.txt";

    std::ifstream fread(file_name);

    string line;
    while(getline(fread, line))
    {
        cout << line << "\n";
    }
    cout <<"\n";

    char chr;
    while(fread.get(chr))// get a single character
        cout << chr << ", ";

    fread.close();
    return 0;
}
