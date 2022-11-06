D = {"Fred": 55, "James": 67, "Jemima": 71}


def markdistribution(D):
    distribution = {}

    for mark in D.values():
        if mark < 50:
            distribution['N'] = distribution.get('N', 0) + 1
        if 50 <= mark < 60:
            distribution['P'] = distribution.get('P', 0) + 1
        if 60 <= mark < 70:
            distribution['Cr'] = distribution.get('Cr', 0) + 1
        if 70 <= mark < 80:
            distribution['D'] = distribution.get('D', 0) + 1
        if mark >= 80:
            distribution['HD'] = distribution.get('HD', 0) + 1

    return distribution


print(markdistribution(D))
