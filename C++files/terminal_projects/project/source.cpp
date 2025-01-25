#include <iostream>
#include <cstring>
#include "./header.h"

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
