def solution(price, money, count):
    mon = [price * (cnt + 1) for cnt in range(count)]

    cost = sum(mon) - money
    if cost > 0:
        return cost
    else:
        return 0