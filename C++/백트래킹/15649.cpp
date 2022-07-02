// n 과 m : 1
#include <iostream>
using namespace std;
int n, m;
int result[9];
bool visited[9];

void DFS(int count){
    if(count == m){
        for(int i = 0; i < m; i++){
            cout << result[i] << " ";
        }
        cout << endl;
        return;
    }
    for(int i = 1; i <= n; i++){
        if(!visited[i]){
            visited[i] = true;
            result[count] = i;
            DFS(count+1);
            visited[i] = false;
        }
    }
}

int main(){
    cin >> n >> m ;
    DFS(0);
}