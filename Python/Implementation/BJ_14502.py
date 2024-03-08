import sys
input = sys.stdin.readline

# 2 (virus) 인덱스를 시작점으로 dfs 계산
def dfs():
    return 0


# 0 index 리스트로 combination 3을 하는 함수
## -> 각 combination 마다 dfs로 바이러스 퍼지는 경우의 0의 개수 check (# map은 deepcopy로 가져오기 )





if __name__ == "__main__":
    n,m = map(int, input().split())
    map = [list(map(int, input().split())) for _ in range(n)]
    
    # 0 index를 저장하는 리스트
    empty_idx = []
    
    # 2 index를 저장하는 리스트
    virus_idx = []
    
    for i in range(n):
        for j in range(m):
            if map[i][j] == 0:
                empty_idx.append([i,j])
            elif map[i][j] == 2:
                virus_idx.append([i,j])
    
    
            
            
    