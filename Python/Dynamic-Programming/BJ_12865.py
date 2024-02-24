# 2차원 DP 문제 (참고 : https://velog.io/@js43o/%EB%B0%B1%EC%A4%80-12865%EB%B2%88-%ED%8F%89%EB%B2%94%ED%95%9C-%EB%B0%B0%EB%82%AD)
'''
행은 배낭의 무게, 열은 아이템의 인덱스
dp[i][j] : 배낭의 최대무게가 i이고, j번째 아이템까지 살펴봤을 때의 최대 가치 
(dp[0][j]는 배낭 최대 무게가 0인 경우 이므로 가치는 전부 0 / dp[i][0]는 아무 아이템도 고려하지 않은 경우이므로 가치는 전부 0)

- update 방식 
1) 현재 넣을 물건의 무게(weight) 만큼 배낭에서 뺀다. 그리고 현재 물건(value)를 넣는다. -> dp[i-weight][j-1]+value
2) 현재 물건을 넣지 않고 이전 배낭 그대로 가지고 간다. -> dp[i][j-1]
1과 2를 비교하여 더 큰 값으로 업데이트
'''
N, K = map(int, input().split())
bag = [[0,0]] + [list(map(int, input().split())) for _ in range(N)] # weight, value

dp = [[0]*(N+1) for _ in range(K+1)]

for i in range(1,K+1): 
    for j in range(1,N+1): 
        weight = bag[j][0]
        value = bag[j][1]
        
        if i < weight:
            dp[i][j] = dp[i][j-1]
        else:
            dp[i][j] = max(dp[i-weight][j-1]+value, dp[i][j-1])
        
print(dp[K][N])