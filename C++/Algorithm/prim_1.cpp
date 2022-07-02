#include <iostream>
#include <queue>
#include <vector>
using namespace std;

vector<pair<int,int>> v[9999];
int dist[9999];
bool select[9999];
int n; // 정점 개수
int m; // 간선 개수
int start; // 시작 정점
int result = 0; // Spanning Tree 의 간선 총합

void Prim(int start){
    // 1단계 : 시작점 기준으로 초기화 작업
    select[start] = true;
    dist[start] = 0;

    // 2단계 : 시작점 기준으로 distance 업데이트 작업
    for(int i = 0; i < v[start].size(); i++)
        dist[v[start][i].first] = v[start][i].second;
    
    // 3단계 : 총 (n - 1)번 반복
    for(int i = 1; i <= n-1; i++){

        // 3-1 단계: select 에 없는 정점들 중에 distnace 제일 작은 정점 찾기 
        int min_dist = 9999;
        int min_vertex;
        for(int j = 1; j <= n; j++){
            if(select[j])   continue;
            if(dist[j] < min_dist){
                min_dist = dist[j];
                min_vertex = j;
            }
        }

        // 3-2 단계 : 찾아낸 정점을 이제 select 에 넣어주기
        select[min_vertex] = true;
        result += min_dist;

        // 3-3 단계: 찾아낸 정점을 기준으로 distance 업데이트 해줌
        for(int j = 0; j < v[min_vertex].size(); j++){
            int next_vertex = v[min_vertex][j].first;
            int next_dist = v[min_vertex][j].second;

            if(select[next_vertex]) continue;
            if(dist[next_vertex] > next_dist)
                dist[next_vertex] = next_dist;
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
    fill(dist, dist + 9999, 9999);

    Prim(start);
    cout << result << endl;
}