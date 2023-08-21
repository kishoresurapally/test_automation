import os

import allure
import pandas as pd


@allure.step
def get_csv(csv_file):
    cur_path = os.path.abspath(os.path.dirname(__file__))
    for root, dirs, files in os.walk(cur_path):
        for name in files:
            if name == csv_file:
                path = root
    file = os.path.join(path, csv_file)
    df = pd.read_csv(file, delimiter=',', encoding='windows-1252')
    list_of_tup = [tuple(row) for row in df.values]
    return list_of_tup


@allure.step
def get_ids(csv_file,tup):
    value = get_csv(csv_file)
    new_id_list = []
    for item in value:
        for val in range(len(item)):
            if val == tup:
                if item[tup] is not None:
                    new_id_list.append(item[5])
    return new_id_list