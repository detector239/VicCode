#include <iostream>
#include <cstdlib>
#include <ctime>


using namespace std;

int main()
{
    srand(time(0)); // time(0) = seconds from Jan 1 1970 till now
    int num = rand(); // the rand() gives a random number but it is extract by an formula and it will be  only a number evry single time we run the program
    cout << num << endl;
    int num1 = rand() % 100; // %10 is the maximum number for the random
    cout << num1 << endl;
    // or we can to use this formula rand() % (minValue - maxValue + 1) + minValue
    short minValue = 0;
    short maxValue = 10;
    int num2 = rand() % (maxValue - minValue + 1) + minValue;
    cout << num2 << endl;
    return 0;
}
