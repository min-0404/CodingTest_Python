// 깊이 우선 탐색 : 재귀(스택) 이용
#include <iostream>
#include <vector>
using namespace std;

bool check[8];
vector<int> v[8];

void DFS(int start){
    int x = start;
    if(! check[x]){
        check[x] = true;
        cout << x << " ";
        for(int i = 0; i < v[x].size(); i++)
            DFS(v[x][i]);
    }

}
int main(){
    v[1].push_back(2);
    v[2].push_back(1);

    v[1].push_back(3);
    v[3].push_back(1);
    
    v[2].push_back(3);
    v[3].push_back(2);

    v[2].push_back(4);
    v[4].push_back(2);

    v[2].push_back(5);
    v[5].push_back(2);

    v[3].push_back(6);
    v[6].push_back(3);

    v[3].push_back(7);
    v[7].push_back(3);

    v[4].push_back(5);
    v[5].push_back(4);

    v[6].push_back(7);
    v[7].push_back(6);

    DFS(1);
}
