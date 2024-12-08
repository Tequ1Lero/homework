grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
grades[0]  = sum(grades[0]) / len(grades[0])
grades[1]  = sum(grades[1]) / len(grades[1])
grades[2]  = sum(grades[2]) / len(grades[2])
grades[3]  = sum(grades[3]) / len(grades[3])
grades[4]  = sum(grades[4]) / len(grades[4])
students = (list(students))
students.sort()
journal = dict(zip(students, grades))
print(journal)









# b = sum(grades[1])/len(grades[1])
# j = sum(grades[2])/len(grades[2])
# k = sum(grades[3])/len(grades[3])
# a = sum(grades[0])/len(grades[0])
# s = sum(grades[4])/len(grades[4])
# average = {(students_list[0]) : a, (students_list[1]) : b, (students_list[2]) : j, (students_list[3]) : k, (students_list[4]) :s }
# print(average)
