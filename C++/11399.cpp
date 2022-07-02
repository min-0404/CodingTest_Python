#include <iostream>
#include <algorithm>
using namespace std;

int n;
int p[1001];

int main(){
    cin >> n;
    for (int i = 1 ; i <= n ; i++){
        int x;
        cin >> x;
        p[i] = x; 
    } 

    sort(p + 1, p + n + 1);
    int total = 0;
    for(int i = 1; i  <= n; i++){
        int sum  = 0;
        for(int j = 1; j <= i; j++){
            sum += p[j];
        }
        total += sum;
    }
    cout << total;
}


