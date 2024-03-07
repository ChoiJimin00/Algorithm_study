'''
Union-Find 알고리즘 : 지민이가 과장된 이야기를 할 수 없는 사람들을 하나의 집합으로 구성

* find 함수로 해당 원소의 parent 원소를 찾는다.
* union 함수로 진실을 아는 사람들과 그와 같이 파티에 오는 사람들(연쇄적)을 하나로 묶는다.
    - 입력받은 두 원소가 모두 진실을 아는 사람 -> 변화 X
    - 둘 중 한 원소가 진실을 아는 사람 -> 진실을 아는 사람을 부모로 갱신
    - 둘 다 진실을 아는 사람이 아님 -> 대소 관계에 따라 부모 관계 부여 (후에 갱신될 수 있으므로)
'''
import sys
input = sys.stdin.readline

def find(parent,x):
    # x의 부모 찾기
    if x!=parent[x]:
        # 한 그래프 내에 존재할 때, 가장 작은 원소를 부모로 설정
        parent[x]=find(parent,parent[x])
    return parent[x]

def union(parent,a,b,mem):
    # a,b의 부모 찾기
    a=find(parent,a)  
    b=find(parent,b)

    # 입력받은 두 원소가 모두 진실을 아는 사람 -> 변화 X
    if a in mem and b in mem:
        return

    # 둘 중 한 원소가 진실을 아는 사람 -> 진실을 아는 사람을 부모로 갱신
    if a in mem:
        parent[b]=a
    elif b in mem:
        parent[a]=b

    # 둘 다 진실을 아는 사람이 아님 -> 대소 관계에 따라 부모 관계 부여
    else:
        if a<b:
            parent[b]=a
        else:
            parent[a]=b

if __name__ == '__main__':
    N,M = map(int,input().split())
    truth_man = list(map(int,input().split()))[1:] # 진실을 아는 사람 index
    party_people = [] # 파티에 참석하는 사람
    
    parent = list(range(N+1))  # 모든 사람의 부모 정보 저장 
    
    # union 연산으로 연결 그래프 구성
    for i in range(M):
        temp = list(map(int,input().split()))
        people = temp[1:]
    
        for j in range(temp[0]-1):
            union(parent,people[j],people[j+1],truth_man)
        party_people.append(temp[1:])

    # find 연산으로 사실을 아는 그룹 구분
    result=0
    for i in party_people:
        for j in range(len(i)):
            if find(parent,i[j]) in truth_man:
                break
        else:
            result+=1

    print(result)