from data_processing import Data

path_json = 'data_raw/dados_empresaA.json'
path_csv = 'data_raw/dados_empresaB.csv'

#Extract

data_enterpriseA = Data(path_json, 'json')
print(f'Empresa A: {data_enterpriseA.name_columns}')
data_enterpriseB = Data(path_csv, 'csv')
print(data_enterpriseB.name_columns)

#Transform

key_mappingB = {'Nome do Item': 'Product Name',
               'Classificação do Produto': 'Product Category',
               'Valor em Reais (R$)': 'Product Price (R$)',
               'Quantidade em Estoque': 'Stock Quantity',
               'Nome da Loja': 'Store Branch',
               'Data da Venda': 'Sale Date'}

key_mappingA = {'Nome do Produto': 'Product Name',
               'Categoria do Produto': 'Product Category',
               'Preço do Produto (R$)': 'Product Price (R$)',
               'Quantidade em Estoque': 'Stock Quantity',
               'Filial': 'Store Branch',
               'Data da Venda': 'Sale Date'}


data_enterpriseB.rename_columns(key_mappingB)
print(f'Enterprise B: {data_enterpriseB.get_columns()}')

data_enterpriseA.rename_columns(key_mappingA)
print(f'Enterprise A: {data_enterpriseA.get_columns()}')

print(data_enterpriseA.number_lines)
print(data_enterpriseB.number_lines)


data_fusion = Data.join(data_enterpriseA, data_enterpriseB)
print(data_fusion.name_columns)
print(data_fusion.number_lines)

#Load

path_combined_data = 'data_processed/combined_data.csv'
data_fusion.save_data(path_combined_data)
print(path_combined_data)