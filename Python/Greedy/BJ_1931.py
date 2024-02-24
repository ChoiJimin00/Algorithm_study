N = int(input())
meeting = []

for _ in range(N):
    start, end = map(int,input().split())
    meeting.append([start, end])
    
# 끝나는 시간을 기준으로 정렬
meeting.sort(key=lambda x : (x[1],x[0]))

# 이전 회의 끝나는 시각 <= 이후 회의 시작 시간. 일 경우 회의 진행 가능
cnt = 0
endPoint = 0
for start, end in meeting:
    if endPoint <= start :
        cnt += 1
        endPoint = end
print(cnt)