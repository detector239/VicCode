#include <iostream>
#include <algorithm>

using namespace std;

bool isNumber(const std::string &s) {
  return !s.empty() && std::all_of(s.begin(), s.end(), ::isdigit);
}

int cin_digit(int variable)
{
    int n;
    char input = char(variable);
    cin >> input;

    if(isNumber(input)){
        n = ++n;
        return input;
    }
    else{
        cout << "Failed! Input a number.\n";
        return 0;
    }
}
int cin_int(string text, int number){
    while (true){
        cout << text;
        int num = cin_digit(number);
        if (num != 0){
            return num;
            }
        }
    }


int main()
{
    int start_num;
    cout << "We will sum numbers!!\n" ;
    cin_int("   From: ", start_num);
}
