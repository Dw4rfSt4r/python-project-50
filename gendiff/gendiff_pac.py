import json
import copy

# создаем словарь с ключом/значением и метаданными
# meta это результат сравнения
def generate_diff_dic(file1, file2):
    diff_dic = {}
    first_file_copy = copy.deepcopy(file1)
    second_file_copy = copy.deepcopy(file2)
    for file_key, file_val in first_file_copy.items():
        if file_key in second_file_copy:
            if file1[file_key] == file2[file_key]:
                # при мэтче в диф копируется ключ и значение
                diff_dic[file_key] = {
                    'file_key_val': file_val,
                    'meta': 'match'}
            else:
                # иначе ключ и оба значения кортежем
                diff_dic[file_key] = {
                    'file_key_val': (file1[file_key], file2[file_key]),
                    'meta': 'modified'}
        else:
            # копия уникальных ключей/значений
            diff_dic[file_key] = {'file_key_val': file_val, 'meta': '-'}
    # копия уникальных ключей/значений второго файла
    for file_key, file_val in second_file_copy.items():
        if file_key not in first_file_copy:
            diff_dic[file_key] = {'file_key_val': file_val, 'meta': '+'}
    return diff_dic


def list_keys(diff_dic):
    key_list = list(file_key for file_key, val in diff_dic.items())
    return key_list


def get_file_val(file_key, diff_dic):
    file_val = diff_dic[file_key]['file_key_val']
    return file_val


def get_meta(file_key, diff_dic):
    meta = diff_dic[file_key]['meta']
    return meta


def get_files(path1, path2):
    with open(path1) as file1, open(path2) as file2:
        file1 = json.load(file1)
        file2 = json.load(file2)
    return file1, file2


def format_diff_to_lst(diff_dic):
    key_list = sorted(list_keys(diff_dic))
    result_diff_lst = []
    for file_key in key_list:
        #собираем ключ, значение для дифа, и мета
        diff_element = ({file_key: get_file_val(file_key, diff_dic)})
        diff_meta = get_meta(file_key, diff_dic)
    # строим каждый элемент дифа по мета и значению
        if diff_meta == '+' or diff_meta == '-':
            result_diff_lst.append(f'{diff_meta} {diff_element}')
        elif diff_meta == 'modified':
            diff1 = ({file_key: get_file_val(file_key, diff_dic)[0]})
            diff2 = ({file_key: get_file_val(file_key, diff_dic)[1]})
            result_diff_lst.append(f'- {diff1}\n+ {diff2}')
        else:
            result_diff_lst.append(f'  {diff_element}')
            result_diff_lst = list(
                map(
                    lambda x:
                    x.replace("True", "true").replace("False", "false"),
                    result_diff_lst))
    return result_diff_lst


def generate_diff(path1, path2):
    file1, file2 = get_files(path1, path2)
    diff_dic = generate_diff_dic(file1, file2)
    diff_lst_concatenated = "\n".join(format_diff_to_lst(diff_dic))
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
