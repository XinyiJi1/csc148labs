"""lab2"""
from typing import Any
from typing import Union


class GradeEntry:
    """represent a student's grade
    name-course identifier
    grade-student's grade for this course
    weight-course weight"""

    def __init__(self, name: str,
                 grade: Union[int, str], weight: float) -> None:
        assert weight == 1.0 or weight == 0.5, 'course weight wrong'
        self.name = name
        self.grade = grade
        self.weight = weight

    def __eq__(self, other: Any) -> bool:
        raise NotImplementedError('subclass needed')

    def __str__(self) -> str:
        raise NotImplementedError('subclass needed')


class NumericGradeEntry(GradeEntry):
    """it is actually a docstriong with integer
    value of grade"""

    def __init__(self, name: str, grade: int, weight: float) -> None:
        """the grade must be an integer"""
        assert type(grade) == int and 0 <= grade <= 100, 'grade error'
        GradeEntry.__init__(self, name, grade, weight)
        a = {4.0: [c for c in range(85, 101, 1)],
             3.7: [c for c in range(80, 85, 1)],
             3.3: [c for c in range(77, 80, 1)],
             3.0: [c for c in range(73, 77, 1)],
             2.7: [c for c in range(70, 73, 1)],
             2.3: [c for c in range(67, 70, 1)],
             2.0: [c for c in range(63, 67, 1)],
             1.7: [c for c in range(60, 63, 1)],
             1.3: [c for c in range(57, 60, 1)],
             1.0: [c for c in range(53, 57, 1)],
             0.7: [c for c in range(50, 53, 1)],
             0.0: [c for c in range(0, 50, 1)], }
        for key in a:
            if self.grade in a[key]:
                self.point = key

    def __eq__(self, other: Any) -> bool:
        """verify whether the name, point and weight of the imformation
        are equal to ach other

        >>> a = NumericGradeEntry('c', 86, 0.5)
        >>> b = NumericGradeEntry('d', 87. 1.0)
        >>> a == b
        False
        """
        if type(other) != NumericGradeEntry and type(other) != LetterGradeEntry:
            return False
        return self.name == other.name and self.point == other.point \
            and self.weight == other.weight

    def __str__(self) -> str:
        """return the representation for people of the imformation

        >>> print(NumericGradeEntry('c', 86, 0.5))
        weight:0.5,grade:86,point:4.0
        """
        return "weight:{},grade:{},point:{}".\
            format(self.weight, self.grade, self.point)


class LetterGradeEntry(GradeEntry):
    """it is actually a docstriong with integer
    value of grade"""

    def __init__(self, name: str, grade: str, weight: float) -> None:
        """the grade must be an string"""
        a = {'A+': 4.0, 'A': 4.0, 'A-': 3.7,
             'B+': 3.3, 'B': 3.0, 'B-': 2.7,
             'C+': 2.3, 'C': 2.0, 'C-': 1.7,
             'D+': 1.3, 'D': 1.0, 'D-': 0.7, 'F': 0.0}
        assert type(grade) == str and grade in a, 'grade error'
        GradeEntry.__init__(self, name, grade, weight)
        self.point = a[self.grade]

    def __eq__(self, other: Any) -> bool:
        if type(other) != NumericGradeEntry and type(other) != LetterGradeEntry:
            return False
        return self.name == other.name and self.point == other.point \
            and self.weight == other.weight

    def __str__(self) -> str:
        return "weight:{},grade:{},point:{}".\
            format(self.weight, self.grade, self.point)


