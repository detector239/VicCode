#include <string>
#include <iostream>
#include <cstdlib>
#include <ctime>
#include <vector>

using namespace std;

void game()
{
    vector<int> guesses;
    int random = (rand() % 500) + 1;
    cout << "Let's play\n";

    int guess;
    while (guess != random)
    {
        cout << "Guess the number: ";
        cin >> guess;
        if (guess == random)
        {
            cout << "Great job\n\n";
        }
        else if (guess < random)
        {
            cout << "Too low\n";
            guesses.push_back(guess);
        }
        else
        {
            cout << "Too high\n";
            guesses.push_back(guess);
        }
    }

    cout <<"These are your guesses: ";
    for (auto el : guesses)
    {
        cout << el << " ";
    }
}

int main()
{
    srand(time(NULL));
    int choice=1;
    bool var = false;

    while(choice == 1)
    {
        cout << "What do you want to do?: \n";
        (var == true) ? cout << "Write 1 to Play again\n" : cout << "Write 1 to Play\n";
        cout << "Write anything else to quit\n> ";

        if (cin >> choice && choice == 1) game();
    }

    return 0;
}
