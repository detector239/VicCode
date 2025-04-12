#include <iostream>
#include <algorithm>
#include <cmath>

using namespace std;

bool comp(int a, int b){
    return a > b;
}

int scad(int& n, int sz){
    int tc[sz], td[sz];
    for (int i=0; i<sz; i++){
        tc[i] = n%10;
        td[i] = n%10;
        n /= 10;
    }
    sort(tc, tc+4);
    sort(td, td+4, comp);

    int nc=0;
    for(int i : tc) nc = nc*10 + i;
    int nd=0;
    for(int i : td) nd = nd*10 + i;
    n = nd-nc;
    return n;
}

int main()
{
    char x;
    int n, prec;
    cin >> n;
    do{
        prec = n;
        cout << scad (n, int(log10(n)+1)) << endl;
        cin >> x;
    }while(n!=prec);
    return 0;
}
