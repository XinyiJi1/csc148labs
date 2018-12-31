"""the test.py"""
if __name__ == '__main__':
    from grade import GradeEntry, NumericGradeEntry, LetterGradeEntry
    grades = [NumericGradeEntry('csc148', 87, 0.5),
              NumericGradeEntry('mat137', 76, 1.0),
              LetterGradeEntry('his450', 'B+', 0.5)]
    for g in grades:
        print(g)
    total = sum([g.point * g.weight for g in grades])
    total_weight = sum([g.weight for g in grades])
    print('GPA={}'.format(total/total_weight))
