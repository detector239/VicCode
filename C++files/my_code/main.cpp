#include <iostream>

using namespace std;

int main(){
  int m, c=0, v[200];
  double med, s=0, n;
  cin >> n;
  for(int i=0; i<n; i++){
    cin >> m;
    v[i] = m;
    s += m;
  }
  med = s/n;
  for (int i=0; i<n; i++)
    if(v[i] > med) c++;

  cout << c;
  return 0;
}