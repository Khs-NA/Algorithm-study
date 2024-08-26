def combination(n, m, chosen = []):
    if len(chosen) == m:
        print(' '.join(map(str, chosen)))
        return

    for i in range(0, len(arr)):
        if arr[i] not in chosen:
            combination(n, m, chosen + [arr[i]])


if __name__ == '__main__':
    N, M = map(int,input().split())
    arr = list(map(int,input().split()))
    arr.sort()
    combination(N,M)