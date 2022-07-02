// 주어진 가중치 그래프에서 최소비용 "spanning tree(신장 트리)" 만드는 방법
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int getParent(int* arr, int node){
    if(arr[node] == node)
        return node;
    return getParent(arr, arr[node]);
}

void unionParent(int* arr, int a, int b){
    a = getParent(arr, a);
    b = getParent(arr, b);
    if(a < b)   arr[b] = a;
    else    arr[a] = b;
}

bool find(int* arr, int a, int b){
    a = getParent(arr , a);
    b = getParent(arr, b);
    if(a == b)  return true;
    else    return false;
}

class Edge
{
public:
    int node1;
    int node2;
    int distance;
    Edge(int a, int b, int distance){
        this -> node1 = a;
        this -> node2 = b;
        this -> distance = distance;
    }
    bool operator<(Edge& ref){
        return this -> distance < ref.distance;
    }
};

int main(){
    int n = 7; // 정점 개수
    int m = 11; // 간선 개수
    int parent[8]; // 각 정점의 부모정점을 저장해줄 배열
    
    vector<Edge> v;
    v.push_back(Edge(1,7,12));
    v.push_back(Edge(1,4,28));
    v.push_back(Edge(1,2,67));
    v.push_back(Edge(1,5,17));
    v.push_back(Edge(2,4,24));
    v.push_back(Edge(2,5,62));
    v.push_back(Edge(3,5,20));
    v.push_back(Edge(3,6,37));
    v.push_back(Edge(4,7,13));
    v.push_back(Edge(5,6,45));
    v.push_back(Edge(5,7,73));

    sort(v.begin(), v.end()); // distance 에 따라 오름차순 정렬

    for(int i = 1; i < 8; i++) // 일단, 모든 정점의 parent 를 자기 자신으로 설정하고 시작
        parent[i] = i;
    
    int sum = 0;
    for(int i = 0; i < v.size(); i++){
        if(find(parent, v[i].node1, v[i].node2)) continue; // 만약 같은 그래프라면 패스
        unionParent(parent, v[i].node1, v[i].node2);
        sum += v[i].distance;
    }
    cout << sum << endl;
}

