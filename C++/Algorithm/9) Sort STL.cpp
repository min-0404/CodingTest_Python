// sort STL의 활용법
#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

bool compare1(int a, int b){ //오름차순 설정
    return a < b;
    //if(a < b)   return true; => 이것과 동일함
    //else    return false;
}
bool compare2(int a, int b){ //내림차순 설정
    return a > b;
    //if(a > b)     return true; => 이것과 동일함
    //else      return false;
}

class Student
{
public:
    string name;
    int score;
    Student(string name, int score){
        this -> name = name;
        this -> score = score;
    }
    bool operator<(Student& ref){ // score에 따른 오름차순 정렬을 위해 정의해줌
        return (this -> score) < ref.score;
    }

};

int main(){
    // 1. 오름차순으로 정렬하기
    int x[10] = {9, 3, 5, 4, 1, 10, 8, 6, 7, 2};
    sort(x, x + 10, compare1);
    for(int i = 0; i < 10; i++)
        cout << x[i] << " ";
    cout << endl;

    // 2. 내림차순으로 정렬하기
    sort(x, x + 10, compare2);
    for(int i = 0; i < 10; i++)
        cout << x[i] << " ";
    cout << endl;

    // 3. 내가 정의한 정렬규칙 사용하기
    // 하지만 클래스를 직접 이용하는 것은 코테에서 좋지 못함
    Student arr[4] = {
        Student("minseok", 90),
        Student("chaeyoon", 95),
        Student("hyelim", 100),
        Student("sunju", 80)
    };
    sort(arr, arr + 4);
    for(int i = 0; i < 4; i ++)
        cout << arr[i].name << " ";
    
}
