def secondLowestGrade(classList):
    secondLowestScore = sorted(set(_[1] for _ in classList))[1]
    result = sorted([_[0] for _ in classList if _[1] == secondLowestScore])
    return result


if __name__ == '__main__':
    record = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        record.append([name,score])
    print('\n'.join(secondLowestGrade(record)))
