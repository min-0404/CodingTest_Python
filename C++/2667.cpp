#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <cstring>
using namespace std;

int n;
int graph[26][26];
bool visited[26][26];
typedef struct{
    int x,y;
}dir;
dir moveDir[4] = {{1,0},{-1,0},{0,1},{0,-1}};
int cnt;
vector<int> v;

void DFS(int x, int y){
    visited[x][y] = true;
    cnt++;
    for(int i = 0; i < 4; i ++){
        int dx = x + moveDir[i].x;
        int dy = y + moveDir[i].y;
        if(dx >= 0 && dx < n && dy >= 0 && dy < n && !visited[dx][dy] && graph[dx][dy] == 1){
            DFS(dx, dy);
        }
    }
}
int main(){
    cin >> n;
    string s;
    for(int i = 0; i < n; i++){
        cin >> s;
        for(int j = 0; j< s.length(); j++){
            if(s[j] == '0') graph[i][j] = 0;
            else graph[i][j] = 1;
        }
    }

    for(int i = 0; i < n; i++){
        for(int j = 0; j < n; j++){
            if(!visited[i][j] && graph[i][j] == 1){
                cnt = 0;
                DFS(i, j);
                v.push_back(cnt);
            }
        }
    }
    cout  << v.size() << endl;
    sort(v.begin(), v.end());
    for(int i = 0; i <v.size(); i++){
        cout << v[i] << endl;
    }

}