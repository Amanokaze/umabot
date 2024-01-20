import os
import re
import csv
from collections import defaultdict
import pandas as pd

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def parsing_condition(data):
    # Translate variables
    def parse_condition(condition):
        match = re.match(r'([a-zA-Z_0-9]+)([<>=]+)(\d+)', condition)
        var, operator, value = match.groups()
        return var, [operator, int(value)]

    # Convert string to list of dictionaries
    delimiter1 = "@"
    delimiter2 = "&"
    temp_list = [item.split(delimiter2) for item in data.split(delimiter1)]
    conditions = []

    for lst in temp_list:
        dict_list = defaultdict(list)
        for var, op_val in map(parse_condition, lst):
            dict_list[var].append(op_val)
        conditions.append(dict(dict_list))

    # Check if dictionaries in list can be merged
    unique_vars = set().union(*[set(d.keys()) for d in conditions])
    diff_count = sum(1 for var in unique_vars if not all(d.get(var) == conditions[0].get(var) for d in conditions))

    if diff_count == 1:
        # Merge dictionaries in list
        merged = defaultdict(list)
        for var in set().union(*[set(d.keys()) for d in conditions]):
            for d in conditions:
                if var in d:
                    merged[var].extend(d[var])
        
        for k, v in merged.items():
            merged[k] = list(map(list, set(map(tuple, v))))
                                
        return [dict(merged)]
    
    return conditions

def make_condition_data(data):
    # Load data
    tv_df = pd.read_csv(os.path.join(BASE_DIR, "umabot", "data", "translate_variables.csv"))
    v1_df = pd.read_csv(os.path.join(BASE_DIR, "umabot", "data", "variable_detail.csv"))
    v2_df = pd.read_csv(os.path.join(BASE_DIR, "umabot", "data", "variable_detail2.csv"))
    or_df = pd.read_csv(os.path.join(BASE_DIR, "umabot", "data", "order_rate.csv"))

    # Parse variables
    data_list = parsing_condition(data)

    # Formatting Data using dfs'
    formatted_data_list = []
    tv_df = tv_df.fillna("")

    for d in data_list:
        for k, v in d.items():
            formatted_str = str()
            tv_data = tv_df[tv_df["English"]==k]
            
            print(tv_data)
            print(type(tv_data))

    return data

def extract_vars():
    def extract_variables_from_csv(input_filename):
        variables = set()
        with open(input_filename, 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            for row in csvreader:
                # 각 행에서 변수 추출
                if row:  # 빈 행은 무시
                    matches = re.findall(r'([a-zA-Z_0-9]+)[<>=]+', row[0])
                    variables.update(matches)
        return variables

    def save_to_csv(variables, output_filename):
        with open(output_filename, 'w', newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            for var in sorted(variables):
                csvwriter.writerow([var])

    # 입력 CSV 파일 이름
    input_filename = os.path.join(BASE_DIR, "umabot", "data", "backdata.csv")
    # 출력할 CSV 파일 이름
    output_filename = os.path.join(BASE_DIR, "umabot", "data", 'extracted_variables.csv')

    # CSV 파일에서 변수 추출
    variables = extract_variables_from_csv(input_filename)
    # 추출된 변수를 새로운 CSV 파일로 저장
    save_to_csv(variables, output_filename)    


if __name__ == "__main__":
    mode = "condition"

    if mode=="condition":
        data1 = "ground_type==2&ground_condition==3@ground_type==2&ground_condition==4"
        data2 = "distance_rate>=50&order_rate>=40&order_rate<=70"
        data3= "distance_rate>=50&order==1&bashin_diff_behind<=1@distance_rate>=50&order==2&is_overtake==1"
        make_condition_data(data1)
        make_condition_data(data2)
        make_condition_data(data3)
    elif mode=="extract":
        extract_vars()
