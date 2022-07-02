// 계수 정렬 : O(N)
// 범위 조건이 있는 경우 매우 빠름 (자리를 바꿔가면서 정렬하는게 아니고, 크기를 기준으로 개수를 세주는 것)
#include <iostream>
using namespace std;

int main(){
    int count[6] = {0};
    int arr[30] = {1, 3, 2, 4, 3, 2, 5, 3, 1, 2, 3, 4, 4, 3, 5, 1,2,3, 5,2, 3, 1, 4,3,5,1, 2,1,1,1};

    for(int i = 0; i < 30; i++)   count[arr[i]]++;
    
    for(int i = 1; i < 6; i++){
        for(int j = 0; j < count[i]; j++){
            cout << i << " ";
        }
    }
}