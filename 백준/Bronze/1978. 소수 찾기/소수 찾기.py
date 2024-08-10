import math

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

N = int(input())
numbers = list(map(int, input().split()))
cnt = 0

for number in numbers:
    if is_prime(number):
        cnt += 1

print(cnt)
