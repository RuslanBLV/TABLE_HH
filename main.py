from src.hh_api import create_table, interface, recreate_database_postgres, info_table
from src.hh_vacansy import all_id
from src.hh_file import interface


def main():
    print(f"id компаний: {all_id()}")
    print(recreate_database_postgres())
    print(create_table())
    print(info_table())
    print(interface())


if __name__ == '__main__':
    print(main())
