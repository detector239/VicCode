#include <iostream>

using namespace std;

int main()
{

    string password = "hig123";
    string guess = "";
    // will run at least once
    do
    {
        cout << "Guess the password: ";
        cin >> guess;
    }while(guess != password);

    return 0;
}
