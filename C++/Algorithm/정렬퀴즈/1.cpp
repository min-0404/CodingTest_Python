// 백준 2752
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
    int arr[3] = {};
    for(int i = 0; i < 3; i++){
        int x;
        cin >> x;
        arr[i] = x;
    }
    SelectionSort(arr, 3);
    for(int i = 0; i < 3; i++){
        cout << arr[i] << " ";
    }
}