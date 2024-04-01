import sys
input = sys.stdin.readline

def opposite(x,y):
    global mat
    N,M = len(mat), len(mat[0])
    
    for i in range(3):
        for j in range(3):
            if x+i < N and y+j < M:
                mat[x+i][y+j] = 0 if mat[x+i][y+j] else 1

def cnt_matrix():
    global mat
    global answer
    
    cnt = 0
    for x in range(N-2):
        for y in range(M-2):
            if mat[x][y] != answer[x][y]:
                opposite(x,y)
                cnt += 1
                
            if mat == answer:
                return cnt
     
    return cnt if mat == answer else -1

if __name__ == '__main__':
    N,M = map(int,input().split())
    
    mat = [list(map(int, input().rstrip())) for _ in range(N)]
    answer = [list(map(int, input().rstrip())) for _ in range(N)]
    
    print(cnt_matrix())