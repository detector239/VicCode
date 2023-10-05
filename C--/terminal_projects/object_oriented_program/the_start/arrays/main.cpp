#include <iostream>

using namespace std;

void print_array(int array[], int size)
{
    for (int i = 0; i < size; i++)
    {
        cout << array[i] << " ";
    }
    cout << endl;
}

int main()
{
    //int guess[100];// guess is array with max 100 int variable
    // or
    int guess[] = {12, 74, 76, 29, 72, 74, 63};
    cout << guess[4] << endl;// we print the fifth element, (72)
    guess[3] = 45; // the fifth element will be now 345
    cout << guess[3] << endl;


    int g_size = sizeof(guess) / 4;
    print_array(guess, g_size);

    return 0;
}
