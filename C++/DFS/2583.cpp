// DFS
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int m, n, k; // m 이 y축, n 이 x축
typedef struct{
    int y, x;
}Dir;
Dir moveDir[4] = {{1,0}, {-1, 0}, {0, 1}, {0, -1}};
int graph[101][101];
bool visited[101][101] = {false};
int cnt;

void DFS(int y, int x){
    visited[y][x] = true;
    cnt++;
    for(int i = 0; i< 4; i++){
        int dy = y + moveDir[i].y;
        int dx = x + moveDir[i].x;
        if(dx >= 0 && dx < n && dy >= 0 && dy < m && graph[dy][dx] == 0 && !visited[dy][dx]){
            DFS(dy, dx);
        }
    }
}
int main(){
    cin >> m >> n >> k;
    for(int i = 0; i < k; i++){
        int x1, y1, x2, y2;
        cin >> x1 >> y1 >> x2 >> y2;
        for(int i = y1; i < y2; i++){
            for(int j = x1; j < x2; j++){
                graph[i][j] = 1;
            }
        }
    }

    vector<int> v;
    for(int i = 0; i < m ; i++){
        for(int j = 0 ; j < n; j++){
            if(graph[i][j] == 0 && !visited[i][j]){
                cnt = 0;
                DFS(i,j);
                v.push_back(cnt);
            }
        }
    }
    cout << v.size() << endl;
    sort(v.begin(), v.end());
    for(int i = 0; i < v.size(); i++){
        cout << v[i] << " ";
    }
    cout << endl;
}

