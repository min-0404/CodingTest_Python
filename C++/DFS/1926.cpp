// DFS 문제: 처음에 벡터 썻는데 런타임오류 떠서 그냥 cnt, width 변수로 수정함
#include <iostream>
using namespace std;
int n, m;
int graph[500][500];
bool visited[500][500] = {false};
typedef struct{
    int x, y;
}dir;
dir moveDir[4] = {{1,0},{-1,0},{0,1},{0,-1}};
int cnt; // 그림의 개수
int width; // 각 그림의 넓이
int max_width; // 가장 큰 그림의 넓이 

void DFS(int x, int y){
    visited[x][y] = true;
    width++;
    for(int i = 0; i < 4; i++){
        int dx = x + moveDir[i].x;
        int dy = y + moveDir[i].y;
        if(dx >= 0 && dx < m && dy >= 0 && dy < n && !visited[dx][dy] && graph[dx][dy] == 1){
            DFS(dx, dy);
        }
    }
    
}

int main(){
    cin >> n >> m;
    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            int z;
            cin >> z;
            graph[j][i] = z;
        }
    }

    for(int i = 0; i < m; i++){
        for(int j = 0; j < n; j++){
            if(graph[i][j] == 1 && !visited[i][j]){
                cnt++;
                width = 0;
                DFS(i, j);
                max_width = max(max_width, width);
            }
        }
    }
    cout << cnt << endl;
    cout << max_width;
}