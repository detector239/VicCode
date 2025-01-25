#include <iostream>

using namespace std;

int main()
{
    string str = "Hello World";
    for (int i = 0; i < str.size();  i++)
    {
        cout << str[i] << endl;
        if (str[i] == 'e')
        {
            cout << "found e\n";
            break;// it will exit the loop
        }
    }
    cout << "th e is found!\n\n\n";

    for (int i = 0; i < str.size();  i++)
    {
        if (str[i] == 'e')
        {
            cout << "here needs to be e\n";
            continue;// it will exit the loop
        }
        cout << str[i] << endl;
    }
    return 0;
}
