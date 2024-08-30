def combination(n, m, start=0, chosen=[]):
    if len(chosen) == m:
        print(' '.join(map(str, chosen)))
        return

    used = set()  # 현재 단계에서 중복 선택을 방지하기 위한 집합

    for i in range(0, len(arr)):
        if arr[i] not in used and visited[i] == False:  # 현재 단계에서 사용되지 않은 숫자만 선택
            used.add(arr[i])
            visited[i] = True
            combination(n, m, i + 1, chosen + [arr[i]])
            visited[i] = False

if __name__ == '__main__':
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    visited = [False] * N
    arr.sort()
    combination(N, M)
