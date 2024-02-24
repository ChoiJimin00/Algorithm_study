alpha = [[0,0] for _ in range(46)]

alpha[1]=[0,1]

for i in range(2,46):
    alpha[i][0] = alpha[i-1][1] # A에 대한 것
    alpha[i][1] = alpha[i-1][0] + alpha[i-1][1]

K = int(input())
a,b = alpha[K]

print(a,b)