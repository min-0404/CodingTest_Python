// 백준 2750
#include <iostream>
#include <algorithm>
using namespace std;

int main(){
    int length;
    cin >> length;

    int* arr = new int[length];
    for(int i = 0; i < length; i++){
        int x;
        cin >> x;
        arr[i] = x;
    }
    sort(arr, arr + length);
    for(int i = 0; i < length; i++){
        cout << arr[i] << endl;
    }
       
}