from argparse import ArgumentParser


# def arg_validator()

def parse_input():
    # Создаем экземпляр ArgumentParser
    parser = ArgumentParser(description="Compares two configuration files and shows a difference.")

    # Добавляем аргументы
    parser.add_argument(
        "first_file", 
        type=str, 
    )
    parser.add_argument(
        "second_file", 
        type=str, 
    )

    args = parser.parse_args()
    return args