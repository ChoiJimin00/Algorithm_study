# box의 뒤부터 해당 value보다 큰 박스에 들어 갈 수 있는 개수 선택 -> 첫번째까지 끌고 오기 => DP
# 현재보다 큰 값중에 count 가장 큰 애, 그 count +=1

n = int(input())

box = list(map(int, input().split()))
cnt = [0]*n


for i in range(len(box)-2,-1,-1):
    bigger = []
    for j in range(i+1,len(box)):
        if box[i] < box[j]:
            bigger.append(j)
    
    try:
        current_bigger = bigger[0]
        for big_idx in bigger:
            if cnt[current_bigger] < cnt[big_idx]:
                current_bigger = big_idx
    
        cnt[i] = cnt[current_bigger]+1
    
    except:
        continue        
    
print(max(cnt)+1)