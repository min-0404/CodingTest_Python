#include <iostream>
using namespace std;
int n, k;
int coin[10];
int cnt;
int main(){
    cin >> n >> k;
    for(int i = 0; i < n; i++){
        int x;
        cin >> x;
        coin[i] = x;
    }
    
    for(int i = n-1; i >= 0; i-- ){
        int left_coins = k / coin[i];
        if(left_coins == 0) continue;
        cnt += left_coins;
        k = k % coin[i];
    }
    cout << cnt << endl;
}