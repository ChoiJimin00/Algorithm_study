hansu = [1]*99

for num in range(100,1001):
    num = str(num)
    
    diff = int(num[0]) - int(num[1])
    
    for i in range(len(num)-1):
        
        if diff != int(num[i])-int(num[i+1]) : 
            hansu.append(0)
            break
        
        if i == (len(num)-2):
            hansu.append(1)


N = int(input())
print(sum(hansu[:N]))