import os

if __name__ == '__main__':
    for (date_index, date_file) in enumerate(os.listdir('dpi')):
        if date_index >= 144:
            input_path = os.path.join('dpi', date_file)
            output_folder = os.path.join('dpi_table_txt', date_file[:-4])
            os.makedirs(output_folder, exist_ok=True)
            table1_path = os.path.join(output_folder, 'table 1.txt')
            table2_path = os.path.join(output_folder, 'table 2.txt')

            with open(input_path, 'r') as txt_file:
                txt_data = txt_file.read()
            txt_lines = txt_data.split('\n')
            find_indexes = []
            for (line_index, txt_line) in enumerate(txt_lines):
                if txt_line.lower().find('current dollars') != -1:
                    find_indexes.append(line_index)
            table1_data = ''
            table2_data = ''
            print (len(find_indexes))
            if len(find_indexes) == 3:
                table1_data = '\n'.join(txt_lines[find_indexes[0] - 1:find_indexes[0] + 13])
                pass
            elif len(find_indexes) == 6:
                table1_data = '\n'.join(txt_lines[find_indexes[0] - 1:find_indexes[0] + 13])
                table2_data = '\n'.join(txt_lines[find_indexes[3] - 1:find_indexes[3] + 7])
                pass
            with open(table1_path, 'w') as table1_file:
                table1_file.write(table1_data)
            with open(table2_path, 'w') as table2_file:
                table2_file.write(table2_data)
            print (date_file)