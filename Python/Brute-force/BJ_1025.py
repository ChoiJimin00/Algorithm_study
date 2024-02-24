N,M = map(int,input().split())

tile = []
for _ in range(N):
    tile.append(str(input()))
    
squares = [-1]

cols_unit = [i for i in range(1,M+1)] # 열의 번호 등차 단위
rows_unit = [i for i in range(1,N+1)] # 행의 번호 등차 단위

# 1) 행은 그대로 열의 번호 등차 (등차의 단위 : 1~M , 시작점 위치 : 1~M , 진행 방향: 좌, 우)

for row in range(N):
    for start in range(M):
        for col in cols_unit: 
            
            #breakpoint()     
            num = tile[row][start]
    
            current = start
            while True:
                try:
                    current += col
                    num += tile[N][current]
    
                except:
                    break
        
            squares.append(int(num))
        
        '''
        if type(int(num)**0.5) == int:
            squares.append(int(num))
            '''
            

    
    
    
breakpoint()



# 2) 열은 그대로 행의 번호 등차 (등차의 단위 : 1~N , 시작점 위치 : 1~N , 진행 방향: 상, 하)



# 3) 행의 번호, 열의 번호 등차 (등차의 단위 : 1~M, 1~N , 시작점 위치 : (1,1), ... (n,m), 진행방향 : 우하, 우상, 좌하, 좌상)


print(max(squares))