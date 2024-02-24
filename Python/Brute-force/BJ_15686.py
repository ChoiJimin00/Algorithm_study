# 한 집에 대해, 모든 치킨집과의 거리 비교 (최소 치킨 거리를 반환)
def chicken_distance(house, chickens) :
    minimum = 100
    for chicken in chickens :
        distance = abs(house[0]-chicken[0]) + abs(house[1]-chicken[1])
        if minimum > distance :
            minimum = distance
    return minimum

# 모든 집에 대한 치킨 거리를 더함
def city_chicken_distance(houses, chickens) :
    city_distance = 0
    for house in houses :
        city_distance += chicken_distance(house, chickens)
    return city_distance


N, M = map(int,input().split())
city = [[info for info in map(int,input().split())] for _ in range(N)]
    
houses = []
chickens = []
for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            houses.append((i,j))
        elif city[i][j] == 2:
            chickens.append((i,j))
           

chosen_chickens, minimum = [], 0

def dfs(depth, index, _chosen_chickens) :
     
    global minimum
    if depth == M : # dfs의 깊이가 선택할 수 있는 최대 치킨 집의 개수(M)일때,
        ccd = city_chicken_distance(houses, chosen_chickens)
        if not minimum or minimum > ccd :
            minimum = ccd
        return
    for m in range(index, len(chickens)) :
        _chosen_chickens.append(chickens[m])
        dfs(depth+1, m+1, _chosen_chickens)
        _chosen_chickens.pop(-1)
        
dfs(0, 0, chosen_chickens)
print(minimum)