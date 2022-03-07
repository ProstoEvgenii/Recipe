
def get_merge_files():
    len_dict = {}
    data_dict = {}

    with open('1.txt') as f:
        first_name = '1.txt'
        data_1 = f.readlines()
        data_dict[first_name] = data_1
        len_dict[first_name] = len(data_1)

    with open('2.txt') as f:
        second_name = '2.txt'
        data_2 = f.readlines()
        data_dict[second_name] = data_2
        len_dict[second_name] = len(data_2)

    with open('3.txt') as f:
        third_name = '3.txt'
        data_3 = f.readlines()
        data_dict[third_name] = data_3
        len_dict[third_name] = len(data_3)

    sorted_keys = sorted(len_dict, key=len_dict.get)
    sorted_dict = {}
    for i in sorted_keys:
        sorted_dict[i] = ''.join(data_dict[i])

    with open('result.txt', 'w+') as f:
        for item, v in sorted_dict.items():
            f.write(f'{item}\n{len_dict[item]}\n{sorted_dict[item]}\n')


get_merge_files()
