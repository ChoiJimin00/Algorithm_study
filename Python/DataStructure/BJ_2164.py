from collections import deque
import sys

input = sys.stdin.readline

N = int(input())
card = deque([i for i in range(1,N+1)])


chk = 1
while len(card) != 1:
    if chk % 2 == 0:
        card.append(card.popleft())
    else:
        card.popleft()
    
    chk += 1
    
print(card[0])