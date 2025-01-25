#include <iostream>

using namespace std;

int main()
{
    /*
     for "char" data type we only use '' not ""
    but for string we only use ""
     char will consider only the last character
     every character has a number associated  to it
     every number till 128 has a character associated to it
     the unsigned type is usually not used
    */
    char x = 'A';
    cout << x << endl;
    cout << (int)x << endl; //it will print the number associated to the character if we transform it to an integer
    char z = 65;
    cout << z << endl; /*if we don't transform in an int, it dosen't matter if we introduce the value a number,
    it will print the character associated to it*/
    cout << (int)z << endl;
    return 0;
}
