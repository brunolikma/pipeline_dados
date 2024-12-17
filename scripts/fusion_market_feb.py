import json
import csv

from data_processing import Data

def size_data(data):
    return len(data)

def join(dataA, dataB):
    combined_list = []
    combined_list.extend(dataA)
    combined_list.extend(dataB)
    return combined_list

def transform_data_to_table(data, column_names):
    combined_data_table = [column_names]

    for row in data:
        row_data = []
        for column in column_names:
            row_data.append(row.get(column, 'Unavailable'))
        combined_data_table.append(row_data)
    
    return combined_data_table

def save_data(data, path):
    with open(path, 'w') as file:
        writer = csv.writer(file)
        writer.writerows(data)

path_json = 'data_raw/dados_empresaA.json'
path_csv = 'data_raw/dados_empresaB.csv'

#Extract

data_enterpriseA = Data(path_json, 'json')
print(data_enterpriseA.name_columns)
data_enterpriseB = data_enterpriseA = Data(path_csv, 'csv')
print(data_enterpriseB.name_columns)

#Transform

key_mapping = {'Nome do Item': 'Product Name',
               'Classificação do Produto': 'Product Category',
               'Valor em Reais (R$)': 'Product Price (R$)',
               'Quantidade em Estoque': 'Stock Quantity',
               'Nome da Loja': 'Store Branch',
               'Data da Venda': 'Sale Date'}

data_enterpriseB.rename_columns(key_mapping)
print(f'Enterprise B: {data_enterpriseB.get_columns()}')

print(f'Enterprise A: {data_enterpriseA.get_columns()}')
'''
# Starting the reading
json_data = read_data(path_json,'json')
column_names_json = get_columns(json_data)
size_json_data = size_data(json_data)

print(f"Column names of JSON data: {column_names_json}")
print(f"Size of JSON data: {size_json_data}")

csv_data = read_data(path_csv, 'csv')
column_names_csv = get_columns(csv_data)
size_csv_data = size_data(csv_data)
print(column_names_csv)
print(size_csv_data)

# Data transformation


csv_data = rename_columns(csv_data, key_mapping)
column_names_csv = get_columns(csv_data)
print(column_names_csv)

merged_data = join(json_data, csv_data)
column_names_merge = get_columns(merged_data)
size_merged_data = size_data(merged_data)
print(column_names_merge)
print(size_merged_data)


# Saving the data

merged_data_table = transform_data_to_table(merged_data, column_names_merge)

path_combined_data = 'data_processed/combined_data.csv'

save_data(merged_data_table, path_combined_data)

print(path_combined_data)
'''