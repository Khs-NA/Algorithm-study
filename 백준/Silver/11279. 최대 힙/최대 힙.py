import heapq
import sys

def main():
    heap = []
    input = sys.stdin.read  # 전체 입력을 한 번에 읽어들입니다.
    data = input().split()  # 공백으로 구분된 입력을 리스트로 분할합니다.

    for x in data[1:]:  # 첫 번째 항목은 N이므로 건너뜁니다.
        if x == '0':
            if heap:
                print(-heapq.heappop(heap))
            else:
                print(0)
        else:
            heapq.heappush(heap, -int(x))

if __name__ == '__main__':
    main()
