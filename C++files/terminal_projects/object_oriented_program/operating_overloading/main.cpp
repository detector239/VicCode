#include <iostream>
#include "position.h"

using namespace std;

int main()
{
    Position pos1(5, 7);
    Position pos2(7, 5);
    Position pos3(pos1.x + pos2.x, pos1.y + pos2.y);

    cout << pos3 << endl;

    pos1 == pos2 ? cout << "The positions are equal\n" : cout << "The positions are different\n";

    cout << "Write a position:\n> ";
    cin >> pos3;
    cout << "The position is " << pos3 << endl;
    return 0;
}
