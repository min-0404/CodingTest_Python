#include <iostream>
using namespace std;
int n, m;
int arr[8];

void DFS(int cnt){

    if(cnt == m){
        for(int i = 1; i <= m; i++){
            cout << arr[i] << " ";
        }
        cout << endl;
        return;
    }
    
    for(int i = 1; i <= n; i ++){
        arr[i] = i;
        DFS(cnt + 1);
    }
}

int main(){
    cin >> n >> m;
    DFS(0);
}
