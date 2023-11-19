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
def generate_diff_dic(file1, file2):
    diff_dic = {}
    # уникальные значения (+/- в мета)
    removed_keys = set(file1) - set(file2)
    for key in removed_keys:
        diff_dic[key] = {'file_key_val': file1.get(key),
                         'meta': '-'}
    added_keys = set(file2) - set(file1)
    for key in added_keys:
        diff_dic[key] = {'file_key_val': file2.get(key),
                         'meta': '+'}
    # элементы, попадут в диф как есть (ключ и значение)
    same_keys = set(file1) & set(file2)
    for key in same_keys:
        key_val1 = {key: file1.get(key)}
        key_val2 = {key: file2.get(key)}
        # оригиналы пишутся, как есть (выход из рекурсии)
        if key_val1 == key_val2:
            diff_dic[key] = {'file_key_val': file1.get(key),
                             'meta': 'match'}
        else:  # место для начала рекурсии - фильтрация разных значений
            diff_dic[key] = {'file_key_val': (file1.get(key), file2.get(key)),
                             'meta': 'modified'}
    return diff_dic
    # пока без рекурсии


# обход древовидных структур
'''def recursive_gen_dic(file1, file2):
    for file_key, file_val in first_file_copy.items():
        if'''


def list_keys(diff_dic):
    key_list = list(file_key for file_key, val in diff_dic.items())
    return key_list


# не нравятся имена тут, но других идей пока нет
def get_file_val(file_key, diff_dic):
    file_val = diff_dic[file_key]['file_key_val']
    return file_val


def get_meta(file_key, diff_dic):
    meta = diff_dic[file_key]['meta']
    return meta


# приводим диф в лист для последующей сборки
def format_diff_to_lst(diff_dic):
    key_list = sorted(list_keys(diff_dic))
    result_diff_lst = []
    for file_key in key_list:
        # собираем ключ, значение для дифа, и мета
        diff_element = ({file_key: get_file_val(file_key, diff_dic)})
        diff_meta = get_meta(file_key, diff_dic)
    # строим каждый элемент дифа по мета и значению
        if diff_meta == '+' or diff_meta == '-':
            # пишем уникальные значения
            result_diff_lst.append(f'{diff_meta} {diff_element}')
        elif diff_meta == 'modified':
            # пишем измененные значения (2 варианта)
            diff1 = ({file_key: get_file_val(file_key, diff_dic)[0]})
            diff2 = ({file_key: get_file_val(file_key, diff_dic)[1]})
            result_diff_lst.append(f'- {diff1}\n+ {diff2}')
        else:
            # осталость записать мэтчи
            result_diff_lst.append(f'  {diff_element}')
            # решаем проблему булевых значений
            result_diff_lst = list(
                map(
                    lambda x:
                    x.replace("True", "true").replace("False", "false"),
                    result_diff_lst))
    return result_diff_lst


# собираем диф
def generate_diff(path1, path2):
    # получаем файлы
    file1, file2 = get_files(path1, path2)
    # создаем структуру
    diff_dic = generate_diff_dic(file1, file2)
    # приводим лист к строке переносами
    diff_lst_concatenated = "\n".join(format_diff_to_lst(diff_dic))
    # оборачиваем в скобки
    result = f'{{\n{diff_lst_concatenated}\n}}'
    return result


__all__ = (
    'generate_diff_dic',
    'generate_diff',
    'format_diff_to_lst',
    'get_files',
    'get_meta',
    'get_file_val',
    'list_keys'
)
