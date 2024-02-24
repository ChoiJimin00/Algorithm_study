N = int(input())
A = list(map(int, input().split()))
result = [1]*N

for i in range(len(A)-2,-1,-1):
    for j in range(i+1, len(A), 1):
        if A[i] < A[j]:
            result[i] = max(result[i],result[j]+1)

print(max(result))