#include <fstream>
#include <iostream>

using namespace std;

ifstream fin("date.in");
ofstream fout("date.out");

int main() {
    int n=0, d=0, rd=0, rn, cont=0, m=0, v[10]={0};
    while(fin >> m){
        do{
            v[m%10]++;
            m/=10;
        }while(m>0);
    }
    for(int i=9; i>=0; i--){
        for(int j=1; j<=v[i]; j++){
            fout << i;
        }
    }
    return 0;
}