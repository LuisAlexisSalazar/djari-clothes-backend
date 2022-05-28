from djari_clothes.settings import *
import json


def read_json(name_file):
    path_files = BASE_DIR + "\djari_clothes\Fill_data\\"
    file = path_files + name_file
    f = open(file)
    data = json.load(f)
    return data
