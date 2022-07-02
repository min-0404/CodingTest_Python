// 선택 정렬 : O(N^2)
#include <iostream>
using namespace std;

void swap(int* a, int* b){
    int temp = *a;
    *a = *b;
    *b = temp;
}

void SelectionSort(int* arr, int len){
    for(int i = 0; i < len; i++){
        int min = i;
        for(int j = i + 1; j < len; j++){
            if(arr[min] > arr[j])
                min = j;
        }
        swap(&arr[min], &arr[i]);
    }
}

int main(){
    int x[] = {10, 5, 3, 8, 2};
    SelectionSort(x, sizeof(x)/sizeof(int));
    for(int i = 0; i < sizeof(x)/sizeof(int); i++){
        cout << x[i] << " ";
    }
}
