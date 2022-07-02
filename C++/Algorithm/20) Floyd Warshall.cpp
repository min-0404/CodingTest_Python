// All-pair to All-pair 의 방식
#include <iostream>
#define INF 1e9
using namespace std;

int arr[999][999];
int N; // 노드 개수
int M; // 간선 개수

void FloydWarshall(){
    for(int k = 1; k <= N; k++){
        for(int i = 1; i <= N; i++){
            for(int j = 1; j <= N; j++){
                arr[i][j] = min(arr[i][j], arr[i][k] + arr[k][j]);
            }
        }
    }    
}

int main(){
    cin >> N >> M;

    // 1단계
    for(int i = 0; i < 999; i++){
        fill(arr[i], arr[i] + 999, INF);
    }
    
    // 2단계
    for(int i = 1; i <= N; i ++){
        for(int j = 1; j <= N; j++){
            if(i == j) arr[i][j] = 0;
        }
    }

    // 3단계
    for(int i = 0; i < M; i++){
        int a, b, c;
        cin >> a >> b >> c;
        arr[a][b] = c;
    }

    // 4단계
    FloydWarshall();

    // 5단계
    for(int i = 1; i <= N; i++){
        for(int j = 1; j <= N; j++){
            cout << arr[i][j] << " ";
        }
        cout << endl;
    }


}