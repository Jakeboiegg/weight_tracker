import json

def read(file):
    with open(file,"r") as json_file:
        data = json.load(json_file)
        return data

def write(file,data):
    with open(file,"w") as json_file:
        json.dump(data,json_file)
