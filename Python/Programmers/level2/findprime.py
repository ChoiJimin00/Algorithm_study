from itertools import permutations


def solution(numbers):
    answer = 0

    perm = []
    for i in range(1, len(numbers) + 1):
        perm += permutations(numbers, i)
    # 질문. [permutations(numbers, i) for i in range(1, len(numbers) + 1)]
    num = set([int(''.join(p)) for p in perm])

    for i in num:
        if i < 2:
            continue

        prime = True
        for j in range(2, int(i ** (1 / 2)) + 1):
            if i % j == 0:
                prime = False
                break
        if prime:
            answer += 1

    return answer