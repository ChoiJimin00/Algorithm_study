fruit = int(input())

total = []
max_width = 0
w_idx = 0
max_height = 0
h_idx = 0

for i in range(6):
    direction, length = map(int, input().split())
    
    if (direction == 1) or (direction == 2):
        if max_width < length:
            max_width = length
            w_idx = i
            
    if (direction == 3) or (direction == 4):
        if max_height < length:
            max_height = length
            h_idx = i
    
    total.append([direction, length])
    
subW = abs(total[(w_idx-1)%6][1] - total[(w_idx+1)%6][1])
subH = abs(total[(h_idx-1)%6][1] - total[(h_idx+1)%6][1])

print((max_height*max_width - subW*subH)*fruit)