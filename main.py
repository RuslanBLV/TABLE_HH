from src.hh_api import create_table, create_base, interface
from src.hh_vacansy import list_name_company, list_name


def main():
    base = create_base()
    print(base)
    table = create_table()
    print(table)
    name_company = list_name_company
    print(name_company)
    name_vacancies = list_name
    print(name_vacancies)
    user_choice_result = interface()
    return user_choice_result


if __name__ == '__main__':
    print(main())
