    // Write a regular expression that checks for the correct date/time in this format:
    // 2020-04-22 18:45:07
    // Attention! The answer should be exactly one regular expression without additional code and logic. Check yourself before sending the result (https://regex101.com/).
    // \\d\\d\\d\\d-\\d\\d-\\d\\d \\d\\d:\\d\\d:\\d\\d
    // \\d{4}-\\d{2}-\\d{2} \\d{2}:\\d{2}:\\d{2}
    // \\d{4}-[0-1]\\d-[0-3]\\d [0-2]\\d:[0-5]\\d:[0-5]\\d

#include <iostream>
#include <string>
#include <regex>

using namespace std;

void regex_match(string text, regex regex_code())
{

}

int main()
{
    string s;
    smatch match;

    regex regex1("\\d\\d\\d\\d-\\d\\d-\\d\\d \\d\\d:\\d\\d:\\d\\d");
    regex regex2("\\d{4}-\\d{2}-\\d{2} \\d{2}:\\d{2}:\\d{2}");
    regex regex3("\\d{4}-[0-1]\\d-[0-3]\\d [0-2]\\d:[0-5]\\d:[0-5]\\d");

    cout << "Write your date (in this format 2020-04-22 18:45:07): ";
    getline(cin, s);

    if (regex_match(s, regex1))
    {
        cout << "First match is a success\n";
        if (regex_match(s, regex2))
        {
            cout << "Second match is a success\n";
            if (regex_match(s, regex3))
            {
                cout << "Third match is a success\n";
                cout << "Well done\n\n";
            }
            else
                cout << "The format of your writing is not right\n";
        }
        else
        cout << "The format of your writing is not right\n";
    }
    else
        cout << "The format of your writing is not right\n";

    return 0;
}

