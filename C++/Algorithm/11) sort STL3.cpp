#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

// 정렬 기준이 "2개일때"
// 성적 내림차순으로 정렬하되, 만약 점수가 같으면, 생년월일이 느린 순서로 정렬해보기
// pair 안에 pair를 또 만들어주면 된다.

bool compare(pair<string, pair<int, int>> a, pair<string, pair<int, int>> b){
    if(a.second.first == b.second.first)
        return a.second.second > b.second.second;
    else
        return a.second.first > b.second.first;
}
int main(){
    vector<pair<string, pair<int, int>>> v;
    v.push_back(pair<string, pair<int, int>>("minseok", make_pair(90, 19961222)));
    v.push_back(pair<string, pair<int, int>>("chaeyoon", make_pair(100, 19901222)));
    v.push_back(pair<string, pair<int, int>>("sunju", make_pair(95, 19871222)));
    v.push_back(pair<string, pair<int, int>>("daehyeon", make_pair(90, 19701222)));

    sort(v.begin(), v.end(), compare);

    for(int i = 0; i < v.size(); i++)
        cout << v[i].first << " ";
}