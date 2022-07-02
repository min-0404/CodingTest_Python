// dp
#include <iostream>
#include <algorithm>
using namespace std;
int n;
int amount[10001];
int dp[10001];

int main(){
    cin >> n;
    for(int i = 1; i <= n; i++){
        int x;
        cin >> x;
        amount[i] =x; 
    }

    dp[1] = amount[1];
    dp[2] = dp[1] + amount[2];
    dp[3] = max(amount[1], amount[2]) + amount[3];
    for(int i = 4; i<=n; i++){
        dp[i] = max(max(dp[i-4] + amount[i-1], dp[i-3] + amount[i-1]), dp[i-2]) + amount[i];
    }

    cout << max(dp[n], dp[n-1]);
}