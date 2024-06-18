import pandas as pd
import os
import numpy as np

# dataframe = pd.DataFrame(columns=[' '] * 11)

# for txt_file in os.listdir('txt'):
#     row_list = [txt_file[:-4]]
#     table_dict = {}
#     with open(f'txt/{txt_file}', 'r') as file_data:
#         txt_data = file_data.read()
#         for i in range(1, 10):
#             temp_data = txt_data
#             while True:
#                 table_index = temp_data.find(f'Table {i}.')
#                 if table_index == -1:
#                     break
#                 temp_data = temp_data[table_index + 1:]
#                 table_dict[i] = table_index
#         keys = list(table_dict.keys())
#         values = list(table_dict.values())
#         sorted_value_index = np.argsort(values)
#         row_list += [keys[i] for i in sorted_value_index]
#         row_list += [' '] * (11 - len(row_list))
#         dataframe.loc[len(dataframe)] = row_list
#     print (txt_file)

# dataframe.to_csv('table_list.csv')

for date_folder in os.listdir('table'):
    file_name = os.path.join('table', date_folder, 'table 7.txt')
    if os.path.exists(file_name):
        with open(file_name, 'r') as date_file:
            txt = date_file.read()
        if txt.find('Table ', 1) != -1:
            with open(file_name, 'w') as date_file:
                date_file.write(txt[:txt.find('Table', 1)])
        print (date_folder)