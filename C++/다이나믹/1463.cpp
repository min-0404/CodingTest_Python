// 1로 만들기 : dp
#include <iostream>
#include <algorithm>
using namespace std;


int n;
int dp[1000001];

int main (){
    cin >> n;
    for(int i = 1; i <= n; i++){
        dp[i] = i;
    }
    for(int i = 2; i <= n ; i++){
        if(i % 2 ==0){
            dp[i] = min(dp[i], dp[i/2]);
        }
        if(i % 3 == 0){
            dp[i] = min(dp[i], dp[i/3]);
        }
        dp[i] = min(dp[i], dp[i-1]) + 1;
    }
    cout << dp[n] - 1;
    
}