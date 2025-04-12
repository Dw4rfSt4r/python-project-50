from argparse import ArgumentParser



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