def combinations(n, m, start=1, chosen=[]):
    if len(chosen) == m:
        print(' '.join(map(str, chosen)))
        return

    for i in range(start, n + 1):
        combinations(n ,m, i + 1, chosen + [i])



if __name__ == '__main__':
    N, M = map(int, input().split())
    combinations(N, M)