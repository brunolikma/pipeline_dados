import json
import csv

def read_json(path_json):
    json_data = []
    with open(path_json, 'r') as file:
        json_data = json.load(file)
    return json_data

def read_csv(path_csv):
    csv_data = []
    with open(path_csv, 'r') as file:
        spamreader = csv.DictReader(file, delimiter=',')
        for row in spamreader:
            csv_data.append(row)
    return csv_data

def read_data(path, file_type):
    data = []

    if file_type == 'csv':
        data = read_csv(path)
    
    elif file_type == 'json':
        data = read_json(path)

    return data

def get_columns(data):
    return list(data[-1].keys())

def rename_columns(data, key_mapping):
    new_csv_data = []

    for old_dict in data:
        temp_dict = {}
        for old_key, value in old_dict.items():
            temp_dict[key_mapping[old_key]] = value
        new_csv_data.append(temp_dict)
    
    return new_csv_data

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

key_mapping = {'Nome do Item': 'Product Name',
               'Classificação do Produto': 'Product Category',
               'Valor em Reais (R$)': 'Product Price (R$)',
               'Quantidade em Estoque': 'Stock Quantity',
               'Nome da Loja': 'Store Branch',
               'Data da Venda': 'Sale Date'}
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
