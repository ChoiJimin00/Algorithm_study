def solution(brown, yellow):
    area = brown + yellow

    for r in range(int(area ** (1 / 2)), area):
        c = area / r
        if brown == (2 * r + 2 * c - 4):
            if c > r:
                c, r = r, c
            return [r, c]

    return False