# 참고 : https://cheon2308.tistory.com/entry/%EB%B0%B1%EC%A4%80-1562%EB%B2%88-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EA%B3%84%EB%8B%A8-%EC%88%98
import sys
input = sys.stdin.readline
mod = 1000000000

def step_num(N):
    # 'DP[마지막 자리의 숫자][BITMASKING]' -> 저장되는 값 : 그 전의 자릿수가 +1 이나 -1로 끝난 것의 합을 더해줌
    # 1<<10 == 2^10 == 1024 -> 계단 수를 사용했는지 여부에 대한 경우의 수 
    
    dp = [[0 for _ in range(1<<10)] for _ in range(10)]
    
    # 시작자리를 1로 설정
    for i in range(1,10):
        dp[i][1<<i] = 1
    
    # 자릿수만큼 순회
    for i in range(1,N):
        # dp_next : 현재 길이에 대해 기록
        dp_next = [[0 for _ in range(1<<10)] for _ in range(10)]
        
        for j in range(10):
            # 모든 비트에 대해 순회 (비트 마스킹)
            for k in range(1024):
                # 0과 9의 경우 앞뒤로 한칸씩 밖에 못 더해주므로 조건문을 이용하여 걸러준다.  
                if j < 9:
                    dp_next[j][k|(1<<j)] = (dp_next[j][k|(1<<j)] + dp[j+1][k]) % mod
                if j > 0 :
                    dp_next[j][k|(1<<j)] = (dp_next[j][k|(1<<j)] + dp[j-1][k]) % mod
                    
        dp = dp_next
        
    return sum(dp[i][1023] for i in range(10))%mod

if __name__ == '__main__':
    N = int(input())
    print(step_num(N))