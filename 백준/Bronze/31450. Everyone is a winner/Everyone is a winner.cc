#include <iostream> // 올바른 헤더 파일 선언

using namespace std; // 올바르게 using 선언

int main() {
    int M, K;

    // 사용자 입력 받기
    cin >> M >> K;

    // M이 K로 나누어떨어지는지 확인
    if (M % K == 0) {
        cout << "Yes" << endl;
    }
    else {
        cout << "No" << endl;
    }

    return 0; // 프로그램 정상 종료
}
