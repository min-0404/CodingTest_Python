// 그리디
#include <iostream>
using namespace std;

int n;
int cards[1001];

int main(){
    cin >> n;
    for(int i = 0; i < n; i++){
        int level;
        cin >> level;
        cards[i] = level;
    }
    int max = 0;
    for(int i = 1; i < n; i++){
        if(cards[max] <= cards[i])   max = i;
    }
    
    int gold = 0;
    for(int i = max+1; i < n; i++){
        int sum = cards[max] + cards[i];
        gold += sum;
    }
    for(int i = max-1; i >= 0; i--){
        int sum = cards[max] + cards[i];
        gold += sum;
    }
    cout << gold;    
}