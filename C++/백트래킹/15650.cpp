// n 과 m : 2
#include <iostream>
using namespace std;

int n, m ;
int arr[9];
int result[9];
bool visited[9];


void DFS(int cnt){
    if(cnt == m){
        for(int i = 0; i < cnt; i++){
            cout << result[i] << " ";
        }
        cout << endl ;
        return;
    }
    for(int i = 1; i <= n; i++){
        if(!visited[i] && result[cnt - 1] < arr[i] ){
            visited[i] = true;
            result[cnt]= arr[i];
            DFS(cnt+1);
            visited[i] = false;
        }
    }
}


int main(){
    cin >> n >> m;
    for(int i = 1; i <= n; i++){
        arr[i] = i;
    }
    DFS(0);
    
    
}


