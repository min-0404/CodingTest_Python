// 삽입 정렬 : O(N^2)
// 이미 정렬된 상태의 배열이라면 매우 빠름!!
#include <iostream>
using namespace std;

void InsertionSort(int* arr, int len){
    int i, j, key;
    for(i = 1; i < len; i++){
        key = arr[i];
        for(j = i - 1; j >= 0; j--){
            if(arr[j] > key)    {arr[j+1] = arr[j];}
            else    {break;}
        }
        arr[j + 1] = key;
    }
}

int main(){
    int x[] = {10, 5, 3, 8, 2};
    InsertionSort(x, 5);
    for(int i = 0; i < sizeof(x)/sizeof(int); i++){
        cout << x[i] << " ";
    }
}