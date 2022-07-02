#include <iostream>
using namespace std;

// 1. 순차 탐색: O(N)
int SequentialSearch(int* arr, int len, int key){
    for(int i = 0; i < len; i++){
        if(key == arr[i])
            return i;
    }
    return 0;
}
// 2. 이진 탐색(정렬된 배열일때 사용하면 매우 좋음) : O(logN)
int BinarySearch(int* arr, int len, int key){
    int left = 0;
    int right = len - 1;
    int middle;
    while(1){
        middle = (left + right) / 2; 
        if(key < arr[middle])   right = middle -1;
        else if(key > arr[middle])  left = middle + 1;
        else    return middle;
    }
}

int main(){
    int x[] = {10, 5, 3, 8, 2};
    cout << SequentialSearch(x, sizeof(x)/sizeof(int), 3) << endl; // 배열 x 에서 3의 인덱스 번호 탐색하기

    int y[] = {2, 3, 5, 8, 10};
    cout << BinarySearch(x, sizeof(x)/sizeof(int), 8) << endl; // 배열 x 에서 8의 인덱스 번호 탐색하기
}
