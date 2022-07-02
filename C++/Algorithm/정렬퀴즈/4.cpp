// 백준 1181
#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

bool compare(string a, string b){
    if(a.size() < b.size()) return true;
    else if(a.size() > b.size()) return false;
    else    return a < b;    
}


int main(){
    int n;
    cin >> n;
    cin.ignore();
    
    string arr[20000];
    for(int i = 0; i < n; i++){
        string str;
        getline(cin, str);
        arr[i] = str;
    }
    sort(arr, arr + n, compare);
    for(int i = 0; i < n; i ++){
        if(arr[i] == arr[i -1]) continue;
        cout << arr[i] << endl;
    }
}    