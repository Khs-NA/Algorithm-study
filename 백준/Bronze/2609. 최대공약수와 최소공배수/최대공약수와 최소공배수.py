A,B = map(int,input().split())

greatest_common_divisor_list = []
least_common_multiple_list = []


i = 2
while i <= min(A,B):
    if A % i == 0 and B % i == 0:
        greatest_common_divisor_list.append(i)
        A = A // i
        B = B // i
    else:
        i += 1

least_common_multiple_list.append(A)
least_common_multiple_list.append(B)

greatest_common_divisor = 1
for i in greatest_common_divisor_list:
    greatest_common_divisor *= i

least_common_multiple = greatest_common_divisor
for i in least_common_multiple_list:
    least_common_multiple *= i

print(greatest_common_divisor)
print(least_common_multiple)