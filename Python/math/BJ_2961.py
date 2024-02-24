from itertools import combinations

N = int(input())

sour = []
bitter = []

for _ in range(N):
    taste = list(map(int, input().split()))
    sour.append(taste[0])
    bitter.append(taste[1])
    
food = [i for i in range(N)]
case = []
for i in range(1,N+1):
    
    for j in list(combinations(food,i)):
        case.append(j)
     
difference = []   
for t in case:
    sour_t = 1
    bitter_t = 0
    
    for i in t:
        sour_t *= sour[i]
        bitter_t += bitter[i]
    
    difference.append(abs(sour_t - bitter_t))
    
print(min(difference))