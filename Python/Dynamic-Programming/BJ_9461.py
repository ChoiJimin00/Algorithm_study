#triangle=[0]*101
triangle =  [0, 1, 1, 1, 2, 2]

for i in range(6, 101):
    triangle.append(triangle[i-1] + triangle[i-5])

T = int(input())

for t in range(T):
    N = int(input())
    print(triangle[N])
