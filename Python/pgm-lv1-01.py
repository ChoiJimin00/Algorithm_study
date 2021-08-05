def solution(numbers):
    answer = []

    for i in range(0,len(numbers)):
         for j in range(i+1,len(numbers)):
                answer.append(numbers[i] + numbers[j])
    answer2 = set(answer)
    answer = list(answer2)
    answer.sort()

    return answer