/*Write a program that reads a number, N, from standard input and prints all its divisors (except for 1 and N).
Sample input: 28
Sample output: 2 4 7 14*/

#include <iostream>
#include <vector>

using namespace std;

int main()
{
    int num;
    vector<int> div;

    cout << "You will write a number and we will find its divisors.\nYour number:\n> ";
    cin >> num;

    for (double i = 2.; i <=num/2; i++){if ((num / i)==int(num / i)) div.push_back(i);}

    for (int n : div){cout << n << " ";}
    return 0;
}
