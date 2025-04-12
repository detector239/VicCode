#include <iostream>

using namespace std;

void QuickSort(int v[], int p /*locul pendulului*/, int sz/*marimea array-ului*/){
  if(p>sz){
    int mij = (p + sz)/2, aux;
    aux = v[mij];
    v[mij] = v[p];
    v[p] = aux;
    int st = p, dr = sz, d=0;
    while(st<dr){
      if (v[st] > v[dr]){
        aux = v[dr];
        v[dr] = v[st];
        v[st] = aux;
        d = 1-d;
      }
      st += d;
      dr -= 1-d;
    }
    QuickSort(v, p, st-1);
    QuickSort(v, st+1, sz);

  }
}


int main()
{
    cout << "Hello world!" << endl;
    return 0;
}
