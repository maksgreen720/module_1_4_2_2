
grades= [[5,3,3,5,4], [2,2,2,3], [4,5,5,2], [4,4,3], [5,5,5,4,5]] #по условиям дан список оценок для каждого ученика
                                                                  # в алфавитном порядке
student = {'Johny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'} # По условиям множество (set) students содержит
                                                 # неупорядоченную последовательность имён всех учеников в классе
student= list (student)                    # Перевел set в list, чтобы упорядочить по имени
sorted(student)
my_students = {}          # создал новый список и далее ввел туда key с именем студента и значением - среднего балла
Aaron = (grades[0])
my_students['Aaron'] = sum(Aaron) / 5
Bilbo = (grades[1])
my_students['Bilbo'] = sum(Bilbo) / 4
Johny = (grades[2])
my_students['Johny'] = sum(Johny) / 4
Khendrik = (grades[3])
my_students['Khendrik'] = sum(Khendrik) / 3
Steve = (grades[4])
my_students['Steve'] = sum(Steve) / 5
print(input('Добрый день! Eсли желаете узнать средний бал студентов нажмите клавишу "enter"'))
print(my_students)     # вывел список key - значение  полностью
print(input('Желаете узнать успеваемость отдельного студента? Нажмите "enter"')) # добавил возможность
                                                                                 # отдельно вывести по имени
print(my_students.get (input('Введите правильно имя студента ')))

