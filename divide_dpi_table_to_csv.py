import os
import numpy as np
import pandas as pd

def change_date(date_string, change_count):
    year = int(date_string[0:4])
    month = int(date_string[5:7])
    month += change_count
    if month <= 0:
        while month <= 0:
            month += 12
            year -= 1
    if month > 12:
        while month > 12:
            month -= 12
            year += 1
    return f'{year}_{month:02d}'

def divide_line(row:str):
    row_list = row.replace(',', '').split(' ')
    while '' in row_list:
        row_list.remove('')
    new_row_list = []
    flag = False
    for (i, word) in enumerate(row_list):
        try:
            t = float(word)
            if not flag:
                new_row_list.append(' '.join(row_list[:i]).rstrip('.'))
                new_row_list.append(t)
                flag = True
            else:
                new_row_list.append(t)
        except:
            pass
    return new_row_list

def get_columns_1(date_string:str):
    columns = ['']
    for i in range(-4, 1):
        columns.append(f'pe_ch_{change_date(date_string, i)}')
    return columns

def get_columns_2(date_string:str):
    columns = ['']
    columns.append(f'pr_do_{change_date(date_string, -2)}')
    columns.append(f're_do_{change_date(date_string, -2)}')
    columns.append(f'pr_pe_{change_date(date_string, -2)}')
    columns.append(f're_pe_{change_date(date_string, -2)}')
    columns.append(f'pr_do_{change_date(date_string, -1)}')
    columns.append(f're_do_{change_date(date_string, -1)}')
    columns.append(f'pr_pe_{change_date(date_string, -1)}')
    columns.append(f're_pe_{change_date(date_string, -1)}')

    return columns
if __name__ == '__main__':
    for (date_index, date_file) in enumerate(os.listdir('dpi_table_txt')):
        if date_index >= 0:
            year = int(date_file[:4])
            month = int(date_file[5:7])
            
            columns = get_columns_2(date_file)
            dataframe = pd.DataFrame(columns=columns)
            
            input_path = os.path.join('dpi_table_txt', date_file, 'table 2.txt')
            output_folder = os.path.join('dpi_csv', date_file)
            os.makedirs(output_folder, exist_ok=True)
            output_path = os.path.join(output_folder, 'table2.csv')
            with open(input_path, 'r') as table_file:
                table_data = table_file.read()
            lines = table_data.split('\n')
            if len(lines) > 1:
                column_len = divide_line(lines[1])
                for i in [1, 3, 4, 6, 7]:
                    row_data = divide_line(lines[i])
                    if i == 1:
                        row_data[0] = 'PI ' + row_data[0]
                    elif i == 3 or i == 4:
                        row_data[0] = 'DPI ' + row_data[0]
                    else:
                        row_data[0] = 'PCE ' + row_data[0] 
                    dataframe.loc[len(dataframe)] = row_data
            dataframe.to_csv(output_path, index=False)
            print (date_file)
            # break