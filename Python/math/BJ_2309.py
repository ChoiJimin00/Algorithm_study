from itertools import combinations

def nanjang_hieght(nanjang):
    combi = combinations(nanjang,7)
    combi = list(combi)  # 모든 combination 결과

    for i in range(len(combi)):
        if sum(combi[i]) == 100:
            return sorted(combi[i])

if __name__ == '__main__':
    height_list = []

    for i in range(9):
        height_list.append(int(input()))

    height_list = nanjang_hieght(height_list)

    for i in range(len(height_list)):
        print(height_list[i])