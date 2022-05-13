import json


def load_students(filename):
    """ Функция загружает студентов из файла в список """
    with open(filename, 'r') as f:
        data = json.load(f)
        return data


def load_professions(filename):
    """ Функция загружает навыки из файла в список """
    with open(filename, 'r') as f:
        data = json.load(f)
        return data


def get_student_by_pk(pk, data_students):
    """ Функция получает словарь с данными студента по его pk"""
    for student in data_students:
        if student["pk"] == pk:
            return student


def get_profession_by_title(title, data_professions):
    """ Функция получает словарь с инфо о профессии по названию"""
    for profession in data_professions:
        if profession["title"] == title:
            return profession


def check_fitness(student, profession):
    """ Функция, которая получает студента и профессию, возвращает словарь """
    student_skills = set(student["skills"])
    profession_skills = set(profession["skills"])

    has_skills = student_skills.intersection(profession_skills)
    lacks_skills = profession_skills.difference(has_skills)

    has_percent = round(len(has_skills) / len(profession_skills) * 100)

    str = f'Пригодность: {has_percent}\n' \
          f'{student["full_name"]} знает {",".join(has_skills)}\n' \
          f'{student["full_name"]} не знает {",".join(lacks_skills)}\n'

    print(str)

    return {"has": has_skills, "lacks": lacks_skills, "fit_percent": has_percent}
