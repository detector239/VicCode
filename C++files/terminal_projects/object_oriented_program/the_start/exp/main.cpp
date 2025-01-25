
#include <iostream>
#include <algorithm>

using namespace std;

bool isNumber(const std::string &s) {
  return !s.empty() && std::all_of(s.begin(), s.end(), ::isdigit);
}

 int main(){
    string s2 = "Java";
    string s1 = "4572232";
    string s3 = "Python123";

    isNumber(s1) ? cout << " Java is a Number\n" : cout << "Java is Not a number\n";
    isNumber(s2) ? cout << "4572232 is a Number\n" : cout << "6767526 is Not a number\n";
    isNumber(s3) ? cout << "Python123 is a Number\n" : cout << "Python123 is Not a number\n";

    return 0;
 }
