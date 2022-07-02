#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;
int n, m, start;
vector<int> v[1001];
bool visited[1001];
bool visited_BFS[1001];

void DFS(int x){
    visited[x] = true;
    cout << x << " ";
    for(int i = 0 ; i < v[x].size(); i++){
        if(!visited[v[x][i]]){
            DFS(v[x][i]);
        }
    }
}

void BFS(int start){
    queue<int> q ;
    q.push(start);
    visited_BFS[start] = true;
    while(!q.empty()){
        int x = q.front();
        q.pop();
        cout << x << " ";
        for(int i = 0; i < v[x].size(); i++){
            if(!visited_BFS[v[x][i]]){
                q.push(v[x][i]);
                visited_BFS[v[x][i]] = true;
            }
        }
    }
}

int main(){
    cin >> n >> m >> start;
    for(int i = 0; i < m; i++){
        int x, y;
        cin >> x >> y;
        v[x].push_back(y);
        v[y].push_back(x);
    }
    for(int i = 1; i <= n; i++){
        sort(v[i].begin(), v[i].end());
    }
    DFS(start);
    cout << endl;
    BFS(start);
    
}
