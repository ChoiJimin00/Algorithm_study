from itertools import permutations

N = int(input())
num = []
for i in range(N):
    num.append(i+1)

num_list = list(permutations(num,N))

answer = tuple(map(int,input().split()))


if answer == num_list[-1]:
    print(-1)
else:
    for prev in range(len(num_list)):
        if answer == num_list[prev]:
            for j in range(N):
                print(num_list[prev+1][j],end=" ")
