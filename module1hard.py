grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = list(students)
students.sort()

the_namber_of_student_1_grades = len(grades[0])

student_1_sum_of_grades = sum(grades[0])

the_average_score_student_1 = student_1_sum_of_grades / the_namber_of_student_1_grades

dic_of_average_scor_of_students = {students[0] : the_average_score_student_1}
dic_of_average_scor_of_students.update({students[1] : sum(grades[1]) / len(grades[1]),
                                        students[2] : sum(grades[2]) / len(grades[2]),
                                        students[3] : sum(grades[3]) / len(grades[3]),
                                        students[4] : sum(grades[4]) / len(grades[4])})


print(dic_of_average_scor_of_students)