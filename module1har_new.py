grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = list(students)
students.sort()

grades_new = []

for an in grades:
    nu = sum(an) / len(an)
    grades_new.append(nu)

dic_ = dict(zip(students, grades_new))
print(dic_)