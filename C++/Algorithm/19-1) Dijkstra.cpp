#include <iostream>
#include <vector>
#define INF 1e9
using namespace std;

vector<pair<int, int>> v[9999];
int result[9999];
int check[9999];
int N;
int M;
int start;

int getSmallest(){
    int min = INF;
    int index;
    for(int i = 1; i <= N; i++){
        if(min > result[i]){
            min = result[i];
            index = i;
        }
    }
    return index;
}

void Dijkstra(int start){
    result[start] = 0;
    check[start] = true;
    for(int i = 0; i < v[start].size(); i++){
        result[v[start][i].first] = v[start][i].second;
    }

    for(int i = 0; i < N - 1; i++){
        int current = getSmallest();
        check[current] = true;
        for(int j = 0; j < v[current].size(); j++){
            int cost = result[current] + v[current][j].second;
            if(cost < result[v[current][j].first]){
                result[v[current][j].first] = cost;
            }
        }
    }
}

int main(){
    cin >> N >> M >> start;
    for(int i = 0; i < M * 2; i++){ // 방향 그래프라면 M으로 해줘도 됨
        int a, b, c;
        v[a].push_back({b,c});
    }
    
    fill(result, result + 9999, INF);

    Dijkstra(start);

    for(int i = 1; i <= N; i++){
        cout << result[i] << " ";
    }
}
