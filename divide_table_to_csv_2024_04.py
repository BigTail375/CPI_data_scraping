import os
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

def get_column_table_1(date_folder): # 3
    year = int(date_folder[:4])
    month = int(date_folder[5:7])
    columns = ['']
    columns.append(f're_im_{change_date(date_folder, -1)}')
    columns.append(f'un_in_{change_date(date_folder, -12)}')
    columns.append(f'un_in_{change_date(date_folder, -1)}')
    columns.append(f'un_in_{date_folder}')
    columns.append(f'un_pe_ch_{change_date(date_folder, -12)}')
    columns.append(f'un_pe_ch_{change_date(date_folder, -1)}')
    columns.append(f'se_ad_pe_ch_{change_date(date_folder, -3)}_{change_date(date_folder, -2)}')
    columns.append(f'se_ad_pe_ch_{change_date(date_folder, -2)}_{change_date(date_folder, -1)}')
    columns.append(f'se_ad_pe_ch_{change_date(date_folder, -1)}_{date_folder}')
    return columns

def get_column_table_2(date_folder):
    year = int(date_folder[:4])
    month = int(date_folder[5:7])
    columns = ['']
    columns.append(f're_im_{change_date(date_folder, -1)}')
    columns.append(f'un_pe_ch_{change_date(date_folder, -12)}')
    columns.append(f'un_pe_ch_{change_date(date_folder, -1)}')
    columns.append(f'se_ad_pe_ch_{change_date(date_folder, -3)}_{change_date(date_folder, -2)}')
    columns.append(f'se_ad_pe_ch_{change_date(date_folder, -2)}_{change_date(date_folder, -1)}')
    columns.append(f'se_ad_pe_ch_{change_date(date_folder, -1)}_{date_folder}')
    return columns

def get_column_table_4(date_folder):
    year = int(date_folder[:4])
    month = int(date_folder[5:7])
    columns = ['']
    columns.append(f'pr_sc')
    columns.append(f'pe_ch_{change_date(date_folder, -12)}_{date_folder}')
    columns.append(f'pe_ch_{change_date(date_folder, -2)}_{date_folder}')
    columns.append(f'pe_ch_{change_date(date_folder, -1)}_{date_folder}')

    columns.append(f'pe_ch_{change_date(date_folder, -13)}_{change_date(date_folder, -1)}')
    columns.append(f'pe_ch_{change_date(date_folder, -3)}_{change_date(date_folder, -1)}')
    columns.append(f'pe_ch_{change_date(date_folder, -2)}_{change_date(date_folder, -1)}')
    return columns

def get_column_table_5(date_folder):
    year = int(date_folder[:4])
    month = int(date_folder[5:7])
    columns = ['']
    columns.append('un_1_mo_pe_ch_c_cpi_u')
    columns.append('un_1_mo_pe_ch_cpi_u')
    columns.append('un_12_mo_pe_ch_c_cpi_u')
    columns.append('un_12_mo_pe_ch_cpi_u')
    return columns

def get_column_table_6(date_folder):
    year = int(date_folder[:4])
    month = int(date_folder[5:7])
    columns = ['']
    columns.append(f're_im_{change_date(date_folder, -1)}')
    columns.append(f'se_ad_pe_ch_{change_date(date_folder, -1)}_{date_folder}')
    columns.append(f'se_ad_ef_it_{change_date(date_folder, -1)}_{date_folder}')
    columns.append(f'me_pr_ch_{change_date(date_folder, -1)}_{date_folder}')
    columns.append(f'se_ad_ch_date')
    columns.append(f'se_ad_ch_pe')

    return columns

def get_column_table_7(date_folder):
    year = int(date_folder[:4])
    month = int(date_folder[5:7])
    columns = ['']
    columns.append(f're_im_{change_date(date_folder, -1)}')
    columns.append(f'se_ad_pe_ch_{change_date(date_folder, -12)}_{date_folder}')
    columns.append(f'se_ad_ef_it_{change_date(date_folder, -12)}_{date_folder}')
    columns.append(f'me_pr_ch_{change_date(date_folder, -12)}_{date_folder}')
    columns.append(f'se_ad_ch_date')
    columns.append(f'se_ad_ch_pe')

    return columns

def get_row_list(row:str): 
    if len(row) == 0:
        return None
    row = row.replace(',', '')
    rows = list(row)
    last_index = 0
    if row[0] == ' ':
        rows[0] = '-'
        last_index = 1
    while True:
        cur_index = row.find('  ', last_index)
        if cur_index == -1:
            break
        rows[cur_index + 1] = '-'
        last_index = cur_index + 2
    row = ''.join(rows)
    row_list = row.split(' ')
    while '' in row_list:
        row_list.remove('')
    for i in row_list:
        if i != '-':
            try:
                t = float(i)
            except Exception as e:
                return None
    
    return row_list

def get_row_list_6(row:str): #7
    if len(row) == 0:
        return None
    row = row.replace(',', '')
    rows = list(row)
    last_index = 0
    if row[0] == ' ':
        rows[0] = '-'
        last_index = 1
    while True:
        cur_index = row.find('  ', last_index)
        if cur_index == -1:
            break
        rows[cur_index + 1] = '-'
        last_index = cur_index + 2
    row = ''.join(rows)
    row_list = row.split(' ')
    while '' in row_list:
        row_list.remove('')
    for (index, num) in enumerate(row_list):
        if num != '-' and index != 4:
            try:
                t = float(num)
            except Exception as e:
                return None
    
    return row_list


if __name__ == '__main__':
    for (date_index, date_folder) in enumerate(os.listdir('table')):
        if date_index >= 218:
            columns = get_column_table_6(date_folder)
            dataframe = pd.DataFrame(columns=columns)
            table_path = os.path.join('table', date_folder, 'table 7.txt')
            output_folder = os.path.join('csv', date_folder)
            os.makedirs(output_folder, exist_ok=True)
            output_path = os.path.join(output_folder, 'table 7.csv')
            with open(table_path, 'r') as table_file:
                table_data = table_file.read()
            last_string = ""
            table_lines = table_data.split('\n')
            for (line_index, line) in enumerate(table_lines):
                row_list = get_row_list_6(line)
                if row_list is None:
                    # print (line)
                    last_string = line.strip()
                elif len(row_list) == 7:
                    row_list[4] = row_list[4] + row_list[5]
                    row_list.pop(5)
                    row_list.insert(0, last_string)
                    dataframe.loc[len(dataframe)] = row_list
                elif len(row_list) == 6:
                    row_list.insert(0, last_string)
                    dataframe.loc[len(dataframe)] = row_list
                else:
                    # print (line)
                    # print (row_list)
                    pass
            dataframe.to_csv(output_path, index=False)
            print (date_folder)
            # break