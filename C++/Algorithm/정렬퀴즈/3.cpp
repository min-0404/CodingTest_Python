// 백준 2751
// 제한시간 짧으므로 mergesort 이용
#include <iostream>
using namespace std;

void Merge(int* arr, int* temp, int start, int middle, int end){
    int i = start;
    int j = middle + 1;
    int k = start;
    while(i <= middle && j <= end){
        if(arr[i] < arr[j]) temp[k] = arr[i++];
        else    temp[k] = arr[j++];
        k++;
    }
    if(i > middle){ // j쪽 배열 원소들이 남았을 때 뒷처리
        for(int t = j; t <= end; t++)
            temp[k++] = arr[t];
    }
    else{
        for(int t = i; t <= middle; t++) // i쪽 배열 원소들이 남았을 때 뒷처리
            temp[k++] = arr[t];
    }
    for(int t = start; t <= end; t++)
        arr[t] = temp[t];
}
void MergeSort(int* arr, int* temp, int start, int end){
    if(start < end){
        int middle = (start + end) / 2;
        MergeSort(arr, temp, start, middle);
        MergeSort(arr, temp, middle + 1, end);
        Merge(arr, temp, start, middle, end);
    }
}

int main(){
    int len;
    cin >> len;
    int* arr = new int[len];
    int* temp = new int[len];

    for(int i = 0; i <len ; i++){
        int x;
        cin >> x;
        arr[i] = x;
    }
    MergeSort(arr, temp, 0 , len -  1);
    for(int i = 0; i < len; i++)
        cout << arr[i] << endl;
}
