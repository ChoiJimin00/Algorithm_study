import sys
input = sys.stdin.readline

def max_sum(S):
    words = {} 
    for s in S: 
        x = len(s)-1 # 10의 제곱을 해줄 값
        for i in s :
            if i in words:
                words[i] += 10**x # 있으면 10**x 더하기
            else :
                words[i] = 10**x # 없으면 10**x 넣기
            x -= 1

    words_sort = sorted(words.values(),reverse=True) # 딕셔너리의 value만 내림차순으로 가져옴
    result = 0
    num = 9
    for k in words_sort:
        result += k * num # 내림차순 한거에 9부터 하나씩 곱해서 result에 더함
        num -= 1
    return result


if __name__ == '__main__':
    N = int(input())
    S = [input().strip() for _ in range(N)]
    print(max_sum(S))