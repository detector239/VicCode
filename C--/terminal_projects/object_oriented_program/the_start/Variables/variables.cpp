#include <iostream>

using namespace std;

int main()
{
    int num = 34.2;
    cout << num << endl;
    long num2 = 34.2L; // for higher limits but to be long needs to put a „l" or „L"
    cout << num2 << endl;

    double num3 = 34.2;
    cout << num3 << endl;
    float num4 = 34.2f;  //float take less memory but to be float needs to put a „f" or „F"
    cout << num4 << endl;

    char text = 'asdf';  // with char we only use ''
    cout << text << endl;

    auto variable = "asd";
    cout << variable << endl;

    auto variable2 = 2;
    cout << variable2 << endl;
    auto variable3 = 2.2;
    cout << variable3 << endl;
    auto variable4 = 2.2f;
    cout << variable4 << endl;
    return 0;
}
