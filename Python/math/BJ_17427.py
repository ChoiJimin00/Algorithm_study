## 생각의 전환 필요! - 문제처럼 순서대로 풀면 시간초과임
N = int(input())
print(sum([k*(N//k) for k in range(1, N+1)]))

'''
## 초기 푼 방식
N = int(input())
div_sum_list = []

for i in range(N):
    val = i+1

    temp_sum = 0
    for s_div in range(1, int(val**(1/2))+1):
        if val % s_div == 0 : #소수에 해당
            b_div = val//s_div # b_div:큰 소수, s_div: 작은 소수
            temp_sum += (b_div+s_div) if b_div != s_div else s_div
    div_sum_list.append(temp_sum)

    if val == N:
        print(sum(div_sum_list))
'''