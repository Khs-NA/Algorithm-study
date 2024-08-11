def find_smallest_generator(n):
    min_generator = float('inf')
    for m in range(max(0, n - 9 * len(str(n))), n):
        if m + sum(int(digit) for digit in str(m)) == n:
            min_generator = min(min_generator, m)

    return min_generator if min_generator != float('inf') else 0


# 입력을 받고 함수 호출
N = int(input())
print(find_smallest_generator(N))
