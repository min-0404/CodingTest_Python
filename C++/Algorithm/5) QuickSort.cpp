// 퀵 정렬 : O(NlogN)
// 최악의 상황 = 이미 정렬된 배열일때 : O(N^2)
#include <iostream>
using namespace std;

void swap(int* a, int* b){
    int temp = *a;
    *a = *b;
    *b = temp;
}

void QuickSort(int* arr, int start, int end){
    if(start >= end)    return;
    int pivot = start;
    int i = start + 1;
    int j = end;
    while(i <= j){
        while(arr[pivot] >= arr[i] && i <= end)  i++;
        while(arr[pivot] <= arr[j] && j > start)  j--;
        if(i > j)   swap(&arr[j], &arr[pivot]);
        else    swap(&arr[i], &arr[j]);
    }
    QuickSort(arr, start, j - 1);
    QuickSort(arr, j + 1, end );   
}

int main(){
    int x[] = {10, 5, 3, 8, 2};
    QuickSort(x, 0, 4);
    for(int i = 0; i < sizeof(x)/sizeof(int); i++){
        cout << x[i] << " ";
    }
}
