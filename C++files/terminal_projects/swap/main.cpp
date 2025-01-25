#include <iostream>
#include <string>

using namespace std;

void swap(int &num1, int &num2)
{
    int temporary = num1;
    num1 = num2;
    num2 = temporary;
}

void swap(string &num1, string &num2)
{
    string temporary = num1;
    num1 = num2;
    num2 = temporary;
}

int main()
{
    int x, y;
    x = 23;
    y = 20;
    swap(x, y);
    cout <<"x = "<< x << "; y = " << y << endl;

    string type = "tree";
    string specie = "bamboo";
    swap(type, specie);
    cout <<"type = "<< type << "; specie = " << specie << endl;
    return 0;
}
