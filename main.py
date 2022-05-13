from config import STUDENTS, PROFESSIONS
from functions import load_students, get_student_by_pk, load_professions, check_fitness, get_profession_by_title

if __name__ == '__main__':
    print('Привет!')
    print('Введите pk студента')
    pk = int(input())
    data_students = load_students(STUDENTS)
    student = get_student_by_pk(pk, data_students)
    if not student:
        print('Нет такого студента')
        quit()
    print(f'{student["full_name"]}\nЗнает: {student["skills"]}')

    print(f'Выберите специальность для оценки студента {student["full_name"]}')
    title = input()
    data_professions = load_professions(PROFESSIONS)
    profession = get_profession_by_title(title, data_professions)
    if not profession:
        print('Нет такой профессии')
        quit()

    check_fitness(student, profession)
