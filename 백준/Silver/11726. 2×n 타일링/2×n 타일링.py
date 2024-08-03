import sys

n = int(sys.stdin.readline().strip())

# n = 1, 1
# n = 2, 2
# n = 3, 3
# n = 4, 5
# n = 5, 8
# n = 6, 13
# n = 7, 21
# n = 8, 34
# n = 9, 55

numbers = [0] * 1001
numbers[1] = 1
numbers[2] = 2

for i in range(3,n+1):
    numbers[i] = int(numbers[i-1]) + int(numbers[i-2])

print(numbers[n]%10007)
