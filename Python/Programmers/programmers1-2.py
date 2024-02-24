def del_duplication(arr):
    answer=[]

    for i in arr:
        if len(answer) == 0:
            answer.append(i)
        if answer[-1] != i :
            answer.append(i)

    print(answer)

if __name__ == '__main__':
    del_duplication([1,1,3,3,0,1,1])
