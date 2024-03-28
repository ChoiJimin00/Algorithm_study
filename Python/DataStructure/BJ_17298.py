# 참고 : https://velog.io/@tks7205/%EB%B0%B1%EC%A4%80-17298-%EC%98%A4%ED%81%B0%EC%88%98-Stack%EC%9C%BC%EB%A1%9C-%ED%92%80%EA%B8%B0
'''
1. stack에는 현재 원소를 담고 인접한 두원소끼리만 비교한다.
2. 인접한 두 원소 중 오른 쪽이 클때 stack을 pop하여 answer를 업데이트한다.
3. 그 이후에 stack의 가장 위에 있는 값이 현재 오른쪽 값보다 작은 지 확인하고, 작다면 pop 한다.
3번은 stack이 비거나 왼쪽의 값이 더 큰 값을 가질때 까지 반복한다.
'''
import sys
input = sys.stdin.readline

if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    
    answer = [-1] * N
    stack = [0] # A리스트의 index 저장
    for i in range(1, N):
        while stack and A[stack[-1]] < A[i]:
            answer[stack.pop()] = A[i]
        stack.append(i)
    
    print(*answer)