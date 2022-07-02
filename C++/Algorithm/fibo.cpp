// 0, 1, 1, 2, 3, 5...
// 피보나치 구현의 세가지 방법: 재귀, dp, 반복문
#include <iostream>
using namespace std;

// 방법 1: 재귀  O(2^N)
int recursive_Fibo(int n){
    if(n == 0)  return 0;
    if(n == 1)  return 1;
    return recursive_Fibo(n-1) + recursive_Fibo(n-2); 
}

// 방법 2 : 다이나믹 프로그래밍 O(N^2)
int result[9999]; // 저장해둘 공간
int dynamic_Fibo(int n){ 
    result[0] = 0;
    if(n > 0){
        result[1] = 1;
        for(int i = 2; i <= n; i++)
            result[i] = result[i-1] + result[i-2];
    }
    return result[n];
}

// 방법 3 : 반복문  O(N)
int iterative_Fibo(int n){
    if(n == 0) return 0;
    if(n == 1) return 1;
    else{
        int a = 0;
        int b = 1;
        int sum = 0;
        for(int i = 2; i <= n; i++){
            sum = a + b;
            a = b;
            b = sum;
        }
        return sum;
    }
}