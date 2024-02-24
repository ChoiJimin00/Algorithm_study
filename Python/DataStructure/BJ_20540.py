mbti = list(input())

ideal = ''

ideal += ('I' if 'E' in mbti else 'E')
ideal += ('S' if 'N' in mbti else 'N')
ideal += ('F' if 'T' in mbti else 'T')
ideal += ('P' if 'J' in mbti else 'J')

print(ideal)
