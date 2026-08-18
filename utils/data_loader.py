import json
def data_loader(file_path):
    with open(file_path) as f:
        data=json.load(f)
    return data
def data_length(file_path):
    data=data_loader(file_path)
    return len(data)