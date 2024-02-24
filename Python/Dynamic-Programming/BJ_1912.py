n = int(input())

num = list(map(int, input().split()))

for i in range(1,len(num)):
    num[i] = max(num[i], num[i]+num[i-1])
    
print(max(num))