from itertools import permutations
numbers = [3, 30, 34, 5, 9]
str_num = [str(num) for num in numbers]

result = []
for content in list(permutations(str_num, len(str_num))):
    result.append(''.join(content))

print(sorted(result)[-1])