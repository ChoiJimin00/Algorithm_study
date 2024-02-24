def solution(array, commands):
    answer = []

    for (st, end, idx) in commands:
        numbers = array[st - 1:end]
        answer.append(sorted(numbers)[idx - 1])
    return answer