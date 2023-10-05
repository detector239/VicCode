#include <iostream>

using namespace std;

int main()
{
    int answer = 9;
    int guess;
    cout << "Guess = ";
    cin >> guess;
    int points;

    points = guess == answer ?/*<=that is if statment*/ 10 /*<=if it is true*/ : 0 /*<=if it is false*/;
    cout << points << endl ;
    // or like this
    guess == answer ? cout << "Great\n" : cout << "Bad\n";
    return 0;
}
