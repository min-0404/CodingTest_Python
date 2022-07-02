// 백트래킹
#include <iostream>
#include <algorithm>
#include <string.h>
using namespace std;

int n, m;
int arr[9];
bool visited[9];
bool visited_2[9];
int result[9]; // 결과를 저장할 배열

void DFS(int cnt){
    if(cnt == m ){
        for(int i = 0; i < m; i++){
            cout << result[i] << " ";
        }
        cout << endl;
        return;
    }
    for(int i = 1; i <= n; i++){
        if(!visited[i] && result[cnt -1] < arr[i]){
            visited[i] = true;
            result[cnt] = arr[i];
            DFS(cnt+1);
            visited[i] = false;
        }

    }
}

int main(){
    cin >> n >> m;
    for(int i = 1; i <= n; i++){
        int x;
        cin >> x;
        arr[i]  = x; 
    }
    sort(arr+1, arr + (n+1));
    DFS(0);
}