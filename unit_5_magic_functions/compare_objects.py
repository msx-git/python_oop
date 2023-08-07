class Student:
    def __init__(self, name):
        self.name = name
        self.grades = {}

    def addCourse(self, courseName, courseGrade):
        self.grades[courseName] = courseGrade

    def average(self):
        if len(self.grades) == 0:
            return -1
        else:
            return sum(self.grades.values()) / len(self.grades)

    def __str__(self):
        return f'Student name:{self.name}, courses:{len(self.grades)}, grade:{self.average()}'

    def __gt__(self, other):
        if isinstance(other, Student):
            return self.average() > other.average()
        elif isinstance(other, (int, float)):
            return self.average() > other
        else:
            raise ValueError(f'Can\'t compare Student and {other.__class__.__name__}')


s1 = Student('Max')
s2 = Student('Tom')

s1.addCourse('Math', 89)
s1.addCourse('Programming', 92)
s1.addCourse('English', 85)

s2.addCourse('Physics', 85)
s2.addCourse('Math', 85)

print(s1)
print(s2)

if s1 > s2:
    print(f'{s1.name} has higher grades than {s2.name}')
else:
    print(f'{s2.name} has higher grades than {s1.name}')

if s1 > 90:
    print(f'{s1.name} is smart student.')

# error case
# if s1 > 'some value':
#     print('error')
