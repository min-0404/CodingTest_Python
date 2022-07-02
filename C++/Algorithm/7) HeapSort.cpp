#include <iostream>
using namespace std;

void swap(int* a, int* b){
    int temp = *a;
    *a = *b;
    *b = temp;
}
void heapify(int* arr, int len){ // 하향식 : 위에서 아래로 차례로 검증하는 알고리즘
    for(int i = 1; i < len; i++){
        int current = i;
        while(current != 0){ // current 노드가 최상단 노드에 도달할때 까지 반복
            int root = (current - 1) /2;
            if(arr[current] > arr[root])    swap(&arr[current], &arr[root]);
            current = root;
        }
    }
}
void HeapSort(int* arr, int len){
    heapify(arr, len);
    for(int i = len - 1; i >= 0; i--){ //크기를 줄여가면서
        swap(&arr[i], &arr[0]);
        heapify(arr, i);
    }
}

int main(){
    int heap[9] = {7, 6, 5, 8, 3, 5, 9, 1, 6};
    HeapSort(heap, 9);
    for(int i = 0; i < 9; i++)  cout << heap[i] << ' ';
}

//max heap을 만들어주는 기본원리는 무엇일까?
//하나의 노드를 기준으로 그 노드의 부모노드와 값을 비교해가면서 root까지 한단계씩 올라가는것

//이 올라가는 과정을 전체에서 봤을때 하향식으로 할지 상향식으로 할지 결정하는 것임
//해당 코드는 하향식임(root의 자식부터 순회를 시작했으므로)

