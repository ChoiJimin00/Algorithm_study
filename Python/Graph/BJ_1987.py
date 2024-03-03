# 시간초과 참고 블로그 : https://leeingyun96.tistory.com/22
# bfs, dfs에서 dp처럼 경로를 저장하는 게 필요하다면 array로 set을 쓴다면 해결이 가능하다.
import sys
input = sys.stdin.readline

def bfs(x,y):
    answer = 1
    temp = [[0,0,-1,1], [1,-1,0,0]] # 남, 북, 서, 동

    q = set([(x,y,board[x][y])])

    while q:
        x1,y1,ans = q.pop()

        for i in range(4):
            tX = x1 + temp[0][i]
            tY = y1 + temp[1][i]

            if 0 <= tX < R and 0 <= tY < C and board[tX][tY] not in ans:
                q.add((tX,tY, ans + board[tX][tY]))
                answer = max(answer, len(ans) + 1)
    return answer

if __name__ == '__main__':
    R,C = map(int,input().split())
    board = []
    
    for _ in range(R):
        board.append(list(map(str,input())))
        
    print(bfs(0,0)) 