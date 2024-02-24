from itertools import permutations

num_list = list(permutations(range(1,10),3))

new_list = []
for num in num_list:
    a,b,c = num
    new_list.append(int(str(a)+str(b)+str(c)))

num_list = new_list

N = int(input())

for _ in range(N):
    comp, s, b = map(int, input().split())
    new_num_list = []
    
    for num in num_list:
        strike = 0
        ball = 0
        
        for i in range(3):
            # 스트라이크 횟수
            if str(num)[i] == str(comp)[i]:
                strike += 1
            # 볼 횟수
            elif str(comp)[i] in str(num):
                ball += 1
                
                
        if (strike == s) & (ball == b):
            new_num_list.append(num)
            
    num_list = new_num_list

print(len(num_list))