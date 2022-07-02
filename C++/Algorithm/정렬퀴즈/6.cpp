// 백준 10989
// 힌트 : 메모리 사용량이 한정되어있어서 무작정 입력되는 숫자들을 배열에 저장해놓으면 안됨
// 실패이유 모르겠음
#include <iostream>
using namespace std;

int main(){
    int arr[10001] = {0};
    int n;
    cin >> n;
    for(int i = 0; i < n; i++){
        int x;
        cin >> x;
        arr[x]++;
    }
    for(int i = 1; i < 10001; i++){
        if(arr[i]){
            for(int j = 0; j < arr[i]; j++)
                cout << i << endl;
        }
    }
}