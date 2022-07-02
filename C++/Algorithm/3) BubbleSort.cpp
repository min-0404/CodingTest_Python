// 버블 정렬 : O(N^2)
#include <iostream>
using namespace std;

void swap(int* a, int* b){
    int temp = *a;
    *a = *b;
    *b = temp;
}
void BubbleSort(int* arr, int len){
    for(int i = 0; i < len; i++){
        for(int j = 0; j < len -1 - i; j++){
            if(arr[j] > arr[j+1])
                swap(&arr[j], &arr[j + 1]);
        }
    }
}

int main(){
    int x[] = {10, 5, 3, 8, 2};
    BubbleSort(x, sizeof(x)/sizeof(int));
    for(int i = 0; i < sizeof(x)/sizeof(int); i++){
        cout << x[i] << " ";
    }
}