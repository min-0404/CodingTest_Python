// dfs
#include <iostream>
#include <vector>
#include <cstring>
using namespace std;

int test_cnt;
int m, n;
int k;
int c;
typedef struct{
    int x, y;
}dir;
dir movedir[4] = {{1,0},{-1,0},{0,1},{0,-1}};
int graph[51][51];
bool visited[51][51];
int cnt = 0;
vector<int> v;

void DFS(int x, int y ){
    visited[x][y] = true;
    for(int i = 0; i < 4; i++){
        int dx = x + movedir[i].x;
        int dy = y + movedir[i].y;
        if(dx >= 0 && dx < m && dy >= 0 && dy < n && !visited[dx][dy] && graph[dx][dy] == 1){
            DFS(dx,dy);
        }
    }
}
int main(){
    cin >> test_cnt;
    
    for(int i = 0; i < test_cnt; i++){
        cnt = 0;
        cin >> m >> n;
        cin >> k;
        for(int i = 0; i < k ; i++){
            int x, y;
            cin >> x >> y;
            graph[x][y] = 1;
        }
        for(int i = 0; i < m; i++){
            for(int j = 0; j < n; j++){
                if(graph[i][j] == 1 && !visited[i][j]){
                    DFS(i,j);
                    cnt++;
                }
            }
        }
    v.push_back(cnt);
    memset(visited, false, sizeof(visited));
    memset(graph, 0, sizeof(graph));
    }
    for(int i = 0; i < v.size(); i++){
        cout << v[i] << endl;
    }
}