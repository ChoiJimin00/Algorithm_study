def combination_sum(numbers):
    comb_sum=[]
    answer=[]

    for i in range(len(numbers)-1):
        for j in range(i+1, len(numbers)):
            comb_sum.append(numbers[i]+numbers[j])

    comb_sum.sort()

    for elem in comb_sum:
        if elem not in answer:
            answer.append(elem)

    return answer

if __name__ == '__main__':
    combination_sum([5,0,2,7])
