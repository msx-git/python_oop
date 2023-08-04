from datetime import datetime


class Developer:
    skillLimit = 3

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.skills = []

    def __str__(self):
        return f'classname-{self.__class__.__name__}, name-{self.name}, age-{self.age}, skills-{len(self.skills)}'

    def addSkill(self, skill):
        if len(self.skills) < Developer.skillLimit:
            self.skills.append(skill)
            print(f'{skill} added successfully')
        else:
            print(f'You can\'t add more than {Developer.skillLimit} skills')

    @classmethod
    def setLimit(cls, limit):
        Developer.skillLimit = limit

    @classmethod
    def fromBirthyear(cls, name, birthyear):
        year = datetime.today().year
        return cls(name, year - birthyear)


d1 = Developer('David', 25)
d1.addSkill('Java')
d1.addSkill('Python')
d1.addSkill('JS')
d1.addSkill('Dart')
Developer.setLimit(4)
d1.addSkill('Dart')
print(d1)

d2 = Developer.fromBirthyear("Tony Stark", 1973)
d2.addSkill('Physics')
d2.addSkill('AI expert')
d2.addSkill('Robotics')
print(d2)
