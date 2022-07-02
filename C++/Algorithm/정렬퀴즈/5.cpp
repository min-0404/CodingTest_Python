// 백준 1431
#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int sum(string str){
    int sum = 0;
    for(int i = 0; i < str.size(); i++){
        if(str[i] - '0' >= 0 && str[i] - '0' <=9)   sum += (str[i] - '0');  
    }
    return sum;
}
bool compare(string a, string b){
    if(a.size() < b.size()) return true;
    else if(a.size() > b.size()) return false;
    else{
        int a_sum = sum(a);
        int b_sum = sum(b);
        if(a_sum != b_sum)   return a_sum < b_sum;
        else    return a < b;
    }

}

int main(){
    string arr[50];
    int len;
    cin >> len;
    cin.ignore();

    for(int i = 0 ; i < len; i++){
        string str;
        getline(cin, str);
        arr[i] = str;
    }
    sort(arr, arr + len, compare);
    for(int i = 0 ; i < len; i++)   cout << arr[i] << endl;
}