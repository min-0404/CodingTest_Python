// 우선순위 큐를 이용한 버전
#include <iostream>
#include <queue>
#include <vector>
using namespace std;

vector<pair<int,int>> v[9999];
bool select[9999];
int n; // 정점 개수
int m; // 간선 개수
int start; // 시작 정점
int result = 0; // Spanning Tree 의 간선 총합

void Prim(int start){
    priority_queue<pair<int,int>> pq;
    
    for(int i = 0; i < v[start].size(); i++)
        pq.push(make_pair(-v[start][i].first, v[start][i].second));

    select[1] = true;

    while(!pq.empty()){
        int dist = -pq.top().first;
        int cur = pq.top().second;
        pq.pop();
        
        
        if(!select[cur]){
            select[cur] = true;
            result += dist;
            for(int i = 0; i < v[cur].size(); i++){
                int next_vertex = v[cur][i].first;
                int next_dist = v[cur][i].second;
                if(!select[next_vertex])    pq.push(make_pair(-next_dist, next_vertex));
            }
        }
    }
}

int main(){
    cin >> n >> m >> start;

    for(int i = 0; i < 2 * m; i ++){ // 무방향 그래프인 경우
        int a, b, c;
        cin >> a >> b >> c;
        v[a].push_back({b,c});
    }

    Prim(start);
    cout << result << endl;
}