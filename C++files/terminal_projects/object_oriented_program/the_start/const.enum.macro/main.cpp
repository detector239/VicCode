#include <iostream>
using namespace std;

//there are 3 methods to declare constant variable
#define x 1 //first method
int main()
{
    const int y = 10;//second method
    enum{z = 100};//third method
    //the constant variable cannot be changed throughout the program
    return 0;
}
