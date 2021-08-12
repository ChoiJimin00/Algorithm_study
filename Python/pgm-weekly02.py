import numpy as np

scores = [[50,90],[50,87]]

def get_grade(grade):
    if grade >= 90:
        return 'A'
    if grade >= 80:
        return 'B'
    if grade >= 70:
        return 'C'
    if grade >= 50:
        return 'D'
    else:
        return 'F'


def solution(scores):
    le = len(scores)

    lank = []
    final = []

    for i in range(le):
        for j in range(le):
            lank.append(scores[j][i])

        large = max(lank)
        small = min(lank)

        if large == scores[i][i]:  # 최대
            if lank.count(large) > 1:  # 유일 X
                final.append(get_grade(np.mean(lank)))
            else:
                lank.remove(large)
                final.append(get_grade(np.mean(lank)))

        else:
            if lank.count(small) > 1:  # 유일 X
                final.append(get_grade(np.mean(lank)))
            else:
                lank.remove(small)
                final.append(get_grade(np.mean(lank)))

        lank = []

    return (''.join(final))