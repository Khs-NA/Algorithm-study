
def get_cut_tree_length(h):
    cut_Tree = 0
    for tree in trees:
        if tree > h:
            cut_Tree += tree - h
        if cut_Tree > M:
            return cut_Tree
    return cut_Tree


def cut_tree(m):
    start, end = 0 , max(trees)
    result = 0

    while start <= end:
        mid = (start + end)// 2
        cut_Tree_Len = get_cut_tree_length(mid)

        if cut_Tree_Len == m:
            return mid
        elif cut_Tree_Len > m: # 기준 나무가 너무 낮아서 많은 양의 나무를 베어버림
            result = mid
            start = mid + 1
        else: # 기준 나무가 너무 높아서 적은 양의 나무를 베어버림
            end = mid - 1


    return result


N, M = map(int,input().split())

trees = list(map(int,input().split()))

Max_H = cut_tree(M)

print(Max_H)