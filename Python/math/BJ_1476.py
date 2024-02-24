def cntday():
    year = 1
    E, S, M = map(int, input().split())

    while True:
        if (year - E) % 15 == 0:
            if (year - S) % 28 == 0:
                if (year - M) % 19 == 0:
                    print(year)
                    break
        year += 1

cntday()