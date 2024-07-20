import sys
from collections import deque
input = sys.stdin.readline

if __name__ == '__main__':
    N, K = map(int, input().split())
    deq = deque([i+1 for i in range(N)])
    
    answer = []
    while deq:
        for _ in range(K-1):
            deq.append(deq.popleft())
        
        answer.append(str(deq.popleft()))
    
    print('<'+', '.join(answer)+'>')