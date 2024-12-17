import json
import csv

class Data:

    def __init__(self, path, data_type):
        self.path = path
        self.data_type = data_type
        self.data = self.read_data()
        self.name_columns = self.get_columns()
        self.number_lines = self.size_data()

    def read_json(self):
        json_data = []
        with open(self.path, 'r') as file:
            json_data = json.load(file)
        return json_data

    def read_csv(self):
        csv_data = []
        with open(self.path, 'r') as file:
            spamreader = csv.DictReader(file, delimiter=',')
            for row in spamreader:
                csv_data.append(row)
        return csv_data

    def read_data(self):
        data = []

        if self.data_type == 'csv':
            data = self.read_csv()
        
        elif self.data_type == 'json':
            data = self.read_json()

        elif self.data_type == 'list':
            data = self.path
            self.path = 'Memory in list'

        return data
    
    def get_columns(self):
        return list(self.data[-1].keys())
    
    def rename_columns(self, key_mapping):
        new_data = []

        for old_dict in self.data:
            temp_dict = {}
            for old_key, value in old_dict.items():
                temp_dict[key_mapping[old_key]] = value
            new_data.append(temp_dict)
        
        self.data = new_data
        self.name_columns = self.get_columns()


    def size_data(self):
        return len(self.data)
    

    def join(dataA, dataB):
        combined_list = []
        combined_list.extend(dataA.data)
        combined_list.extend(dataB.data)
        return Data(combined_list, 'list')
    
    def transform_data_to_table(self):
        combined_data_table = [self.name_columns]

        for row in self.data:
            row_data = []
            for column in self.name_columns:
                row_data.append(row.get(column, 'Unavailable'))
            combined_data_table.append(row_data)
        
        return combined_data_table
    
    
    def save_data(self, path):
        combined_data_table = self.transform_data_to_table()
        with open(path, 'w') as file:
            writer = csv.writer(file)
            writer.writerows(combined_data_table)