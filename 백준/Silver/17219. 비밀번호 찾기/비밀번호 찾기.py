N, M = map(int, input().split())
site = {}
for i in range(N):
    x, y = map(str, input().split())
    site[x] = y

find_site = []
for _ in range(M):
    find_site.append(input())

for i in range(M):
    if find_site[i] in site:
        print(site[find_site[i]])