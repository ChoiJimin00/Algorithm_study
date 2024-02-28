N = int(input())
name_list = []

for _ in range(N):
    age, name = input().split()
    name_list.append([int(age), name])
    
name_list.sort(key = lambda x:x[0])

for age, name in name_list:
    print(age, name)