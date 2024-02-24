list=[]

list.append(0)
list.append(1)
list.append(2)
list.append(4)

for i in range(4,12):
    list.append(list[i-1]+list[i-2]+list[i-3])

for i in range(int(input())):
    print(list[int(input())])