import os
import pandas as pd

def get_row_list_1(row):
    divide_row = row.split('  ')
    while '' in divide_row:
        divide_row.remove('')
    while ' ' in divide_row:
        divide_row.remove(' ')
    return divide_row

def get_row_list_3(row):
    if len(row) < 46:
        return row.strip()
    divide_row = row[46:].split('  ')
    while '' in divide_row:
        divide_row.remove('')
    while ' ' in divide_row:
        divide_row.remove(' ')
    divide_row.insert(0, row[:46].strip())
    return divide_row

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

def get_column_table_1(date_folder):
    year = int(date_folder[:4])
    month = int(date_folder[5:7])
    columns = ['']
    columns.append(f're_im_{year - 1}_{12}')
    columns.append(f'un_in_{change_date(date_folder, -1)}')
    columns.append(f'un_in_{date_folder}')
    columns.append(f'un_pe_ch_{change_date(date_folder, -12)}')
    columns.append(f'un_pe_ch_{change_date(date_folder, -1)}')
    columns.append(f'se_un_pe_ch_{change_date(date_folder, -3)}_{change_date(date_folder, -2)}')
    columns.append(f'se_un_pe_ch_{change_date(date_folder, -2)}_{change_date(date_folder, -1)}')
    columns.append(f'se_un_pe_ch_{change_date(date_folder, -1)}_{date_folder}')
    return columns

def get_column_table_2(date_folder):
    year = int(date_folder[:4])
    month = int(date_folder[5:7])
    columns = ['']
    for i in range(-3, 1):
        columns.append(f'se_ad_in_{change_date(date_folder, i)}')
    columns.append(f'se_ad_an_ra_pe_ch_3_{change_date(date_folder, -9)}')
    columns.append(f'se_ad_an_ra_pe_ch_3_{change_date(date_folder, -6)}')
    columns.append(f'se_ad_an_ra_pe_ch_3_{change_date(date_folder, -3)}')
    columns.append(f'se_ad_an_ra_pe_ch_3_{date_folder}')
    columns.append(f'se_ad_an_ra_pe_ch_6_{change_date(date_folder, -6)}')
    columns.append(f'se_ad_an_ra_pe_ch_6_{date_folder}')
    return columns

def get_column_table_3(date_folder):
    year = int(date_folder[:4])
    month = int(date_folder[5:7])
    columns = ['']
    columns.append(f'pr_sc')
    for i in range(-3, 1):
        columns.append(f'in_{change_date(date_folder, i)}')
    columns.append(f'pe_ch_{change_date(date_folder, -12)}_{date_folder}')
    columns.append(f'pe_ch_{change_date(date_folder, -2)}_{date_folder}')
    columns.append(f'pe_ch_{change_date(date_folder, -1)}_{date_folder}')
    columns.append(f'pe_ch_{change_date(date_folder, -13)}_{change_date(date_folder, -1)}')
    columns.append(f'pe_ch_{change_date(date_folder, -3)}_{change_date(date_folder, -1)}')
    columns.append(f'pe_ch_{change_date(date_folder, -2)}_{change_date(date_folder, -1)}')

    return columns

def get_column_table_7(date_folder):
    year = int(date_folder[:4])
    month = int(date_folder[5:7])
    columns = ['']
    if year % 2 == 1:
        columns.append(f're_im_{year - 4}_12_{year - 3}_12')
    else:
        columns.append(f're_im_{year - 3}_12_{year - 2}_12')
    columns.append(f'un_in_{change_date(date_folder, -1)}')
    columns.append(f'un_in_{date_folder}')
    columns.append(f'un_pe_ch_{change_date(date_folder, -12)}')
    columns.append(f'un_pe_ch_{change_date(date_folder, -1)}')

    return columns

if __name__ == '__main__':
    for (date_index, date_folder) in enumerate(os.listdir('table')):
        if date_index < 218 and date_index >= 102:
            columns = get_column_table_7(date_folder)
            dataframe = pd.DataFrame(columns=columns)
            table_path = os.path.join('table', date_folder, 'table 7.txt')
            output_folder = os.path.join('csv', date_folder)
            os.makedirs(output_folder, exist_ok=True)
            output_path = os.path.join(output_folder, 'table 7.csv')
            with open(table_path, 'r') as table_file:
                table_data = table_file.read()
            last_string = ""
            for line in table_data.split('\n'):
                row_list = get_row_list_3(line)
                if len(row_list) == 1:
                    if len(row_list[0].strip()) == 0:
                        last_string = ""
                    else:
                        last_string = row_list[0].strip()
                elif len(row_list) == 6:
                    if row_list[0].strip().endswith('.') or len(last_string) > 1:
                        row_list[0] = (last_string + ' ' + row_list[0].rstrip('.')).strip()
                        for row_index in range(1, 6):
                            row_list[row_index] = row_list[row_index].replace('$', '').replace('R', '').replace('/','').strip()
                            # if row_list[row_index] == '-':
                            #     row_list[row_index] = ''
                            # else:
                            #     row_list[row_index] = float(row_list[row_index])
                        # print (row_list)
                        dataframe.loc[len(dataframe)] = row_list
                        last_string = ""
                    else:
                        last_string = row_list[0].strip()
                else:
                    last_string = ""
            dataframe.to_csv(output_path, index=False)
            print (date_folder)