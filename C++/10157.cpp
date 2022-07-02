#include <iostream>
using namespace std;
int c, r, k;

int main(void){
    cin >> c >> r;
    cin >> k;

    int i = 1;
    int j = 1;
    int cnt = 1;

    int x = r;
    int y = c;
    int w = r;
    int z = c;

 while(cnt != k){   
    while(j < x){
        if(cnt == k) break;
        cnt++;
        j++;
    }
    x--;
    while(i < y){
        if(cnt == k) break;
        cnt++;
        i++;
    }
    y--;
    while(j > w){
        if(cnt == k) break;
        cnt++;
        j--;
    }
    w++;
    while(i > z){
        if(cnt == k) break;
        cnt++;
        i--;
    }
    z++;
}
    cout << i << " " << j;
}