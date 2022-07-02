// DFS
#include <iostream>
#include <cstring>
#include <vector>
using namespace std;
int w, h;
int graph[51][51];
bool visited[51][51];
typedef struct{
    int x, y;
}dir;
dir direction[8] = { {1, 0}, {1, 1}, {0, 1}, {-1, 1}, {-1, 0}, {-1, -1}, {0, -1}, {1, -1} };
vector<int> v;

void DFS(int x, int y)
{
    visited[x][y] = true;
    for (int i = 0; i < 8; i++){
        int dx = x + direction[i].x;
        int dy = y + direction[i].y;
        if (dx >= 0 && dx < w && dy >= 0 && dy < h && !visited[dx][dy] && graph[dx][dy] == 1)
            DFS(dx, dy);
    }
}

int main(void)
{
    while (1){
        cin >> w >> h;
        if (w == 0 && h == 0)   break;

        memset(visited, false, sizeof(visited));
        int cnt = 0;

        for (int i = 0; i < h; i++)
            for (int j = 0; j < w; j++)
                cin >> graph[j][i];

        for(int i=0; i < w; i++)
            for (int j = 0; j < h; j++)
                if (!visited[i][j] && graph[i][j]){
                    DFS(i, j);
                    cnt++;
                }
                v.push_back(cnt);
    }

    for(int i = 0; i < v.size(); i++){
        cout << v[i] << endl;
    }
}