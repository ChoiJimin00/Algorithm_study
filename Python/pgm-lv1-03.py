def solution(v):
    answer = []
    x_list = []
    y_list = []

    for x,y in v:
        x_list.append(x)
        y_list.append(y)

    for i in range(3):
        if x_list.count(x_list[i]) == 1:
            answer.append(x_list[i])
            break
    for i in range(3):
        if y_list.count(y_list[i]) == 1:
            answer.append(y_list[i])
            break

    return answer



print(solution([[1, 1], [2, 2], [1, 2]]))