#include <iostream>
#include <vector>
#include <queue>
#define INF 1e9
using namespace std;

vector<pair<int, int>> v[9999];
int result[9999];
int N; // 노드 개수
int M; // 간선 개수
int start; // 시작 노드

void Dijkstra(int start){
    priority_queue<pair<int, int>> pq;
    pq.push({0, start});
    result[start] = 0;

    while(!pq.empty()){
        //  1단계
        int distance = -pq.top().first;
        int current = pq.top().second;
        pq.pop();

        // 2단계
        if(distance > result[current]) continue;

        // 3단계
        for(int i = 0; i < v[current].size(); i++){
            int cost = distance + v[current][i].second;
            if(cost < result[v[current][i].first]){
                result[v[current][i].first] = cost;
                pq.push(make_pair(-cost, v[current][i].first));
            }
        }
    }
}

int main(){
    cin >> N >> M >> start;
    for(int i = 0; i < M; i++){ // 만약 undirected 그래프라면 M * 2로 설정
        int a, b, c;
        cin >> a >> b >> c;
        v[a].push_back({b,c});
    }

    fill(result, result + 9999, INF);

    Dijkstra(start);

    for(int i = 1; i <= N; i++){
        cout << result[i] << " ";
    }

}