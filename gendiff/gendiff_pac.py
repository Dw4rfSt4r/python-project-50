import json
import yaml


# проверяем, что в обраотку идут верные форматы
def check_format(path):
    if path.lower().endswith(('.yml', '.yaml')):
        return 'yaml'
    elif path.lower().endswith('.json'):
        return 'json'
    else:
        raise ValueError(f"Wrong format for file: {path}")


# открываем файлы
def get_files(path1, path2):
    if check_format(path1) == 'yaml' and check_format(path2) == 'yaml':
        with open(path1) as file1, open(path2) as file2:
            file1 = yaml.load(file1, Loader=yaml.Loader)
            file2 = yaml.load(file2, Loader=yaml.Loader)
    else:
        with open(path1) as file1, open(path2) as file2:
            file1 = json.load(file1)
            file2 = json.load(file2)
    return file1, file2


# создаем словарь с ключами/значениями и метаданными
# meta это результат сравнения (+/-/match/modified)
# этот словарь это внутренняя структура дифа
def generate_inner_dif(file1, file2):
    inner_dif = {}
    #  добавленные и удаленные ключи (+/- в мета)
    added_keys = set(file2) - set(file1)
    removed_keys = set(file1) - set(file2)
    # Запись удаленных ключей в диф
    inner_dif.update({
        key: {'value': file1[key], 'meta': '-'}
        for key in removed_keys})
    # Запись добавленных ключей в диф
    inner_dif.update({
        key: {'value': file2[key], 'meta': '+'}
        for key in added_keys})
    # пересекающиеся ключи:
    same_keys = set(file1) & set(file2)
    for key in same_keys:
        first_value = file1.get(key)
        second_value = file2.get(key)
        # оригиналы пишутся, как есть если совпали ключи (выход из рекурсии)
        if first_value == second_value:
            inner_dif[key] = {'value': file1.get(key),
                              'meta': 'match'}  # итог: словари без пометок
        # если только в одном  варианте словарь, пишем кортеж с 1 и 2 значениями
        elif not isinstance(file1.get(key),
                            dict) or not isinstance(file2.get(key),
                                                    dict):
            inner_dif[key] = {
                'value': (file1.get(key), file2.get(key)),
                'meta': 'modified'}
        # иначе пишем диф двух словарей
        else:
            inner_dif[key] = {
                'value': (
                    generate_inner_dif(
                        file1.get(key), file2.get(key))),
                'meta': 'modified'}
    return inner_dif


def get_keys(inner_dif):
    keys = list(key for key in inner_dif.keys())
    return keys


# не нравятся имена тут, но других идей пока нет
def get_value(key, inner_dif):
    file_val = inner_dif[key]['value']
    return file_val


def get_meta(key, inner_dif):
    meta = inner_dif[key]['meta']
    return meta


# приводим диф в лист для последующей сборки
def format_diff_to_lst(inner_dif):
    keys = sorted(get_keys(inner_dif))
    result_diff_lst = []
    for key in keys:
        # собираем ключ, значение для дифа, и мета
        diff_element = ({key: get_value(key, inner_dif)})
        diff_meta = get_meta(key, inner_dif)
    # строим каждый элемент дифа по мета и значению
        if diff_meta == '+' or diff_meta == '-':
            # пишем уникальные значения
            result_diff_lst.append(f'{diff_meta} {diff_element}')
        elif diff_meta == 'modified':
            # пишем измененные значения (2 варианта)
            diff1 = ({key: get_value(key, inner_dif)[0]})
            diff2 = ({key: get_value(key, inner_dif)[1]})
            result_diff_lst.append(f'- {diff1}\n+ {diff2}')
        else:
            # осталость записать мэтчи
            result_diff_lst.append(f'  {diff_element}')
            # решаем проблему булевых значений
            result_diff_lst = list(
                map(
                    lambda x: x.replace(
                        "True", "true").replace(
                            "False", "false").replace(
                                "None", 'null'),
                    result_diff_lst))
    return result_diff_lst


# собираем диф
def generate_diff(path1, path2):
    # получаем файлы
    file1, file2 = get_files(path1, path2)
    # создаем структуру
    inner_dif = generate_inner_dif(file1, file2)
    # приводим лист к строке c переносами
    diff_lst_concatenated = "\n".join(format_diff_to_lst(inner_dif))
    # оборачиваем в скобки
    result = f'{{\n{diff_lst_concatenated}\n}}'
    return result


__all__ = (
    'generate_inner_dif',
    'generate_diff',
    'format_diff_to_lst',
    'get_files',
    'get_meta',
    'get_value',
    'get_keys'
)
