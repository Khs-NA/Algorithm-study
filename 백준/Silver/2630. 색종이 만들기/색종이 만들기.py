
def main():
    global white_paper, blue_paper
    white_paper, blue_paper = 0, 0
    count_paper(0,0,N)

    print(white_paper)
    print(blue_paper)

def count_paper(x, y, half):
    global white_paper, blue_paper


    color = paper[x][y]
    same_color = True

    for i in range(x, x+half):
        for  j in range(y, y+half):
            if paper[i][j] != color:
                same_color = False
                break
        if same_color == False:
            break

    if same_color:
        if color == 0:
            white_paper += 1
        else:
            blue_paper += 1

    else:
        half //= 2
        if half > 0:
            count_paper(x,y,half)   # 좌상
            count_paper(x+half,y,half)  # 우상
            count_paper(x,y+half,half)   # 좌하
            count_paper(x+half,y+half,half)   # 우하





if __name__== "__main__":
    N = int(input())
    paper = [list(map(int, input().split())) for _ in range(N)]
    main()