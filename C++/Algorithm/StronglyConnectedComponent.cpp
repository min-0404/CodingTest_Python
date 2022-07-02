#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

bool check[8];
vector<int> v[8];
void DFS(int start){
    int x = start;
    cout << x << " ";
    if(!check[x]){
        check[x] = true;
        for(int i = 0; i < v[x].size(); i++){
            DFS(v[x][i]);
        }
    }
}

int main(){
     
}