n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
answer = 0

tetromino = [
    [(0,0),(0,1),(0,2),(0,3)], # ㅡ
    [(0,0),(1,0),(2,0),(3,0)],
    [(0,0),(0,1),(1,0),(1,1)], # ㅁ
    [(0,0),(1,0),(2,0),(2,1)], # ㄴ
    [(0,1),(1,1),(2,0),(2,1)],
    [(0,0),(0,1),(0,2),(1,0)],
    [(0,0),(0,1),(0,2),(1,2)],
    [(1,0),(1,1),(1,2),(0,2)],
    [(0,0),(1,0),(1,1),(1,2)],
    [(0,0),(0,1),(1,1),(2,1)],
    [(0,0),(0,1),(1,0),(2,0)],
    [(0,0),(1,0),(1,1),(2,1)], # ㄹ
    [(0,1),(1,0),(1,1),(2,0)],
    [(0,1),(0,2),(1,0),(1,1)],
    [(0,0),(0,1),(1,1),(1,2)],
    [(0,0),(0,1),(0,2),(1,1)], # ㅜ
    [(0,0),(1,0),(2,0),(1,1)],
    [(1,0),(1,1),(1,2),(0,1)],
    [(0,1),(1,1),(2,1),(1,0)],
]

def solve():
    for i in range(n):
        for j in range(m):
            find(i,j)

def find(x, y):
    global answer
    for i in range(19):
        sum = 0
        for j in range(4):
            try:
                next_x = x + tetromino[i][j][0]
                next_y = y + tetromino[i][j][1]
                sum += board[next_x][next_y]
            except IndexError:
                continue
        answer = max(sum, answer)

if __name__ == '__main__':
    solve()
    print(answer)