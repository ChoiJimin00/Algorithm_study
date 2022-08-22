while True:
    try:
        n = int(input())
    except:
        break

    cnt = 1
    while True:
        num = int('1'*cnt)
        num %= n
        if num == 0:
            print(cnt)
            break
        cnt +=1
