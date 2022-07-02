// findUnion 문제
#include <iostream>
using namespace std;
int n, m;
int parent[101];
int cnt = 0;

int getParent(int a){
    if(parent[a] == a) return a;
    else return getParent(parent[a]);  
}
void unionParent(int a, int b){
    a = getParent(a);
    b = getParent(b);
    if(a <= b) parent[b] = a;
    else parent[a] = b;
}

int main(){
    cin >> n;
    cin >> m;
    for(int i = 1 ; i <= n; i++)    parent[i] = i;
    for(int i = 0; i < m; i++){
        int a, b;
        cin >> a >> b;
        unionParent(a,b);
    }
    for(int i = 2; i <= n; i++){
        if(getParent(i) ==1)  cnt++; 
    }
    cout << cnt;
}