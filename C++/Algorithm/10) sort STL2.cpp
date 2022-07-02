//클래스 대신 pair 라이브러리 사용법
// pair STL : 한 쌍의 데이터를 처리할 수 있는 자료구조
#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

// 정렬 기준이 1개인 경우(이 때 pair 의 fisrt가 정렬기준이어야함)
// 성적 오름차순으로 정렬해보기
int main(){
    vector<pair<int, string>> v;
    v.push_back(pair<int, string>(90, "minseok"));
    v.push_back(pair<int, string>(100, "hyelim"));
    v.push_back(pair<int, string>(95, "chaeyoon"));

    sort(v.begin(), v.end()); // sort 쓰면 pair의 first원소 기준으로 정렬이 실행됨
    for(int i = 0; i < v.size(); i++)
        cout << v[i].second << " " ;

}