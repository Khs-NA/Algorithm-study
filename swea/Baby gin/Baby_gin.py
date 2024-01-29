def baby_gin(play):
    check = [0]*10
    # 카드 숫자 세기
    for i in play:
        check[i] += 1

    # triplet
    if 3 in check:
       # run
        for i in range(8):
            if 0 not in check[i:i+3]:
                return True
            else:
                return False
    else:
        return False


card = list(map(int,input().split()))
print(card)
print(baby_gin(card))
