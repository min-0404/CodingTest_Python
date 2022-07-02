#include <iostream>
using namespace std;
int parent[11];

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

bool findParent(int* arr, int a, int b){
    a = getParent(arr , a);
    b = getParent(arr, b);
    if(a == b)  return true;
    else    return false;
}

int main(){
    for(int i = 1; i <= 10; i++){ // 초기에 각 정점들의 부모는 자기 자신으로 설정
        parent[i] = i;
    }
    // 정점 1,2,3,4 는 연결 되어있음을 구현
    unionParent(parent, 1, 2);
    unionParent(parent, 2, 3);
    unionParent(parent, 3, 4);

    // 정점 5,6,7,8 은 연결 되어있음을 구현
    unionParent(parent, 5, 6);
    unionParent(parent, 6, 7);
    unionParent(parent, 7, 8);

    cout << findParent(parent, 1, 3); // true
    cout << findParent(parent, 1, 5); // false
}