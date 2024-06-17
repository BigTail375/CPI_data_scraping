import os

def get_first_part():
    for (i, txt_file_name) in enumerate(os.listdir('txt')):
        if i < 32:
            output_root_path = os.path.join('table', txt_file_name[:-4])
            os.makedirs(output_root_path, exist_ok=True)
            with open(os.path.join('txt', txt_file_name), 'r') as txt_file:
                txt_data = txt_file.read()
            last_index = txt_data.find('Table 1.')
            last_index = txt_data.find('Table 1.', last_index + 1)
            last_table_index = 1

            for table_index in [2, 4, 5, 3, 6, 1]:
                cur_index = txt_data.find(f'Table {table_index}.', last_index + 1)
                with open(os.path.join(output_root_path, f'table {last_table_index}.txt'), 'w') as table_file:
                    if table_index != 1:
                        table_file.write(txt_data[last_index:cur_index])
                    else:
                        table_file.write(txt_data[last_index:])
                last_index = cur_index
                last_table_index = table_index

def get_second_part():
    for (i, txt_file_name) in enumerate(os.listdir('txt')):
        if i >= 32 and i < 102:
            output_root_path = os.path.join('table', txt_file_name[:-4])
            os.makedirs(output_root_path, exist_ok=True)
            with open(os.path.join('txt', txt_file_name), 'r') as txt_file:
                txt_data = txt_file.read()
            last_index = txt_data.find('Table 1.')
            last_table_index = 1

            for table_index in [2, 3, 4, 5, 6, 1]:
                cur_index = txt_data.find(f'Table {table_index}.', last_index + 1)
                with open(os.path.join(output_root_path, f'table {last_table_index}.txt'), 'w') as table_file:
                    if table_index != 1:
                        table_file.write(txt_data[last_index:cur_index])
                    else:
                        table_file.write(txt_data[last_index:])
                last_index = cur_index
                last_table_index = table_index

def get_third_part():
    for (i, txt_file_name) in enumerate(os.listdir('txt')):
        if i >= 102:
            output_root_path = os.path.join('table', txt_file_name[:-4])
            os.makedirs(output_root_path, exist_ok=True)
            with open(os.path.join('txt', txt_file_name), 'r') as txt_file:
                txt_data = txt_file.read()
            last_index = txt_data.find('Table 1.')
            last_table_index = 1

            for table_index in [2, 3, 4, 5, 6, 7, 1]:
                cur_index = txt_data.find(f'Table {table_index}.', last_index + 1)
                with open(os.path.join(output_root_path, f'table {last_table_index}.txt'), 'w') as table_file:
                    if table_index != 1:
                        table_file.write(txt_data[last_index:cur_index])
                    else:
                        table_file.write(txt_data[last_index:])
                last_index = cur_index
                last_table_index = table_index

if __name__ == '__main__':
    # get_first_part()
    # get_second_part()
    get_third_part()