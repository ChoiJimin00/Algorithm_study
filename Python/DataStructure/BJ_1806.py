# two pointer 방식으로 해결
import sys
input = sys.stdin.readline

def prefix_sum(num,S):
    left, right = 0,0
    sum = 0
    min_length = 100001
    
    while True:
        # 총합이 S보다 큰 경우, left를 하나씩 옮김
        if sum >= S:
            min_length = min(min_length, right-left)
            sum -= num[left]
            left += 1
        elif right == N:
            break
        
        # 총합이 S보다 작은 경우, right를 하나씩 옮겨 총합이 S를 넘을 때까지 더함
        else:
            sum += num[right]
            right += 1
    
    result = 0 if min_length == 100001 else min_length
    return result

if __name__ == '__main__':
    N, S = map(int, input().split())
    num = list(map(int, input().split()))
    
    print(prefix_sum(num, S))