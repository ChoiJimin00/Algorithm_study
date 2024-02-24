cnt = int(input())
div_list = sorted(list(map(int, input().split())))

if cnt % 2 == 0 : # 짝수
    print(div_list[0]*div_list[-1])
else:
    print(div_list[len(div_list)//2]**2)
