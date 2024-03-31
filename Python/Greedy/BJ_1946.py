import sys
input = sys.stdin.readline

def cnt_person(people):
    ## count 기준 : 서류 점수 순위가 낮은 순으로 탐색, 현재의 top 면접 순위보다 더 낮으면 result += 1
    people.sort(key=lambda x:(x[0],[1]))
    
    top = people[0][1]
    result = 1
    for i in range(1, len(people)):
        if people[i][1] < top:
            top = people[i][1]
            result += 1
    return result
    
if __name__ == '__main__':
    T = int(input())
    
    for _ in range(T):
        N = int(input())
        people = [list(map(int,input().split())) for _ in range(N)]
        
        print(cnt_person(people))