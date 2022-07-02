#include <iostream>
#include <vector>
#include <queue>
using namespace std;

vector<int> v[9999];
int inEdge[9999];
int N; // 노드 개수
int M; // 정점 개수

void TopologySort(){
    queue<int> q;
    vector<int> result;


    // 일단, 들어오는 간선이 0인 노드를 큐에 삽입
    for(int i = 1; i <= N; i++){
        if(!inEdge[i])  q.push(i);
    }
    
    while(!q.empty()){
        int current = q.front();
        q.pop();
        result.push_back(current);

        for(int i = 0; i < v[current].size(); i++){
            inEdge[v[current][i]]--;
            if(!inEdge[v[current][i]]){
                q.push(v[current][i]);
            }
        }
    }

    for(int i = 0; i < result.size(); i++){
        cout << result[i] << " ";
    }
    
}

int main(){
    cin >> N >> M;

    for(int i = 0; i < M; i++){
        int a, b;
        cin >> a >> b;
        v[a].push_back(b);
        inEdge[b]++;
    }

    TopologySort();
}