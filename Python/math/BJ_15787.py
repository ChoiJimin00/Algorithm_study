from collections import deque

N,M = map(int,input().split())

train = [deque([0]*20) for _ in range(N)]

for _ in range(M):
    order = list(map(int, input().split()))
    i = order[1]
    
    if order[0]==1:
        x = order[2]
        train[i-1][x-1] = 1
    elif order[0]==2:
        x = order[2]
        train[i-1][x-1] = 0
    elif order[0]==3:
        train[i-1].pop()
        train[i-1].appendleft(0)
    elif order[0]==4:
        train[i-1].popleft()
        train[i-1].append(0)
 
train_list = []
for obj in train:
    train_list.append(tuple(obj))

print(len(set(train_list)))