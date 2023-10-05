#include <iostream>
#include <vector>


using namespace std;

int main()
{
    const int num_size = 4;
    const int ar_size = 3;
    vector<vector<int>> numbers = {{1, 2, 3}, {5, 6, 7}, {9, 10, 11}, {14, 15, 16}};
    //             /\
    // for vector /||\
    //             ||
    // ____________________________________________________________________________
    // for array - int [how many arrays have][how many elements does an array has]
    for(int num = 0; num < num_size; num++)
    {
        for(int iel = 0; iel < ar_size; iel++)
        {
            int el = numbers[num][iel];
            cout << el << "   ";
        }
        cout << "\n";
    }
    return 0;
}
