num_list = [0]

for i in range(1000):
    for _ in range(i):
        num_list.append(i)
        
A,B = map(int,input().split())
        
print(sum(num_list[A:B+1]))