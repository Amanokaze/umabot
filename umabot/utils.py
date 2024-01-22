import os
import re
import csv
from collections import defaultdict
import pandas as pd

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

operator_to_str = {
    "==": "",
    ">=": " 이상",
    "<=": " 이하",
    ">": " 초과",
    "<": " 미만",
    "!=": "이 아닌"
}

def parsing_condition(data):
    # Translate variables
    def parse_condition(condition):
        match = re.match(r'([a-zA-Z_0-9]+)([<>=!]+)(\d+)', condition)
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

def make_condition_data(skill_id, skill_type, data):
    if data == "" or data is None:
        return ""
    
    # Load data
    tv_df = pd.read_csv(os.path.join(BASE_DIR, "umabot", "data", "translate_variables.csv"))
    vd_df = pd.read_csv(os.path.join(BASE_DIR, "umabot", "data", "variable_detail.csv"))
    vrd_df = pd.read_csv(os.path.join(BASE_DIR, "umabot", "data", "variable_race_detail.csv"))

    # Parse variables
    data_list = parsing_condition(data)

    # Formatting Data using dfs'
    formatted_data_list = []
    tv_df = tv_df.fillna("")
    vd_df = vd_df.fillna("")

    for i, d in enumerate(data_list):
        formatted_temp_list = []
        for k, v in d.items():
            formatted_str = str()
            tv_data = tv_df[tv_df["English"]==k]
            
            prefix = tv_data.loc[:, "KoreanPrefix"].values[0]
            postfix = tv_data.loc[:, "KoreanPostfix"].values[0]
            ref = tv_data.loc[:, "Ref"].values[0]

            formatted_str = f"{prefix} "

            for operator, value in v:
                if ref == 0:
                    formatted_str += f"{value}{postfix}{operator_to_str[operator]}, "

                elif ref == 1:
                    f_value = value
                    vd_data = vd_df.query(f'variable == "{k}" and value == {value}')

                    if len(vd_data) == 1:
                        f_value = vd_data['desc'].values[0]
                    elif len(vd_data) > 1:
                        vd_operator_data = vd_data[vd_data["operator"]==operator]

                        if len(vd_operator_data) == 1:
                            f_value = vd_operator_data['desc'].values[0]
                
                    formatted_str += f"{f_value}{postfix}{operator_to_str[operator]}, "

            formatted_str = formatted_str[:-2].strip()
            formatted_temp_list.append(formatted_str)
        
        race_postfix = str()
        vrd_data = vrd_df[vrd_df["skill_id"]==skill_id]

        if len(vrd_data) > 0:
            if skill_type == "precondition_1":
                race_postfix = vrd_data['precondition_desc_1'].values[0]
            elif skill_type == "precondition_2":
                race_postfix = vrd_data['precondition_desc_2'].values[0]
            elif skill_type == "condition_1":
                if i+1 == 1:
                    race_postfix = vrd_data['condition_desc_1_1'].values[0]
                elif i+1 == 2:
                    race_postfix = vrd_data['condition_desc_1_2'].values[0]
            elif skill_type == "condition_2":
                if i+1 == 1:
                    race_postfix = vrd_data['condition_desc_2_1'].values[0]
                elif i+1 == 2:
                    race_postfix = vrd_data['condition_desc_2_2'].values[0]
            
            race_postfix = f"({race_postfix})"
        
        formatted_temp_str = f"{' / '.join(formatted_temp_list)} {race_postfix}".strip()
        formatted_data_list.append(formatted_temp_str)

    formatted_data = "\n또는\n".join(formatted_data_list).strip()

    return formatted_data

def make_ability_data(at1,at2,at3,av1,av2,av3):
    ability_df = pd.read_csv(os.path.join(BASE_DIR, "umabot", "data", "ability.csv"))
    ability_str = str()
    if at1 != 0:
        ab_df = ability_df[ability_df["id"]==at1]
        ability_str = f"{ab_df['name'].values[0]} {av1/10000 if av1 != 0 else ''}"

    if at2 != 0:
        ab_df = ability_df[ability_df["id"]==at2]
        ability_str = ability_str + " / " + f"{ab_df['name'].values[0]} {av2/10000 if av2 != 0 else ''}"

    if at3 != 0:
        ab_df = ability_df[ability_df["id"]==at3]
        ability_str = ability_str + " / " + f"{ab_df['name'].values[0]} {av3/10000 if av3 != 0 else ''}"
    
    return ability_str

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

def extract_orders():
    # CSV 파일 읽기
    df = pd.read_csv(os.path.join(BASE_DIR, "umabot", "data", "backdata.csv"))
    
    # 정규 표현식으로 'order'와 'order_rate' 조건 추출
    pattern = re.compile(r'\border[^&]*\b|\border_rate[^&]*\b')

    # 조건 추출 및 결합
    df['filtered_condition'] = df['condition'].apply(lambda x: '&'.join(pattern.findall(x)))

    # 결과 저장
    df['filtered_condition'].to_csv(os.path.join(BASE_DIR, "umabot", "data", "order_data.csv"), index=False)

if __name__ == "__main__":
    mode = "ability"

    if mode=="condition":
        data1= "ground_type==2&ground_condition==3@ground_type==2&ground_condition==4"
        data2= "distance_rate>=50&order_rate>=40&order_rate<=70"
        data3= "distance_rate>=50&order==1&bashin_diff_behind<=1@distance_rate>=50&order==2&is_overtake==1"
        data4= "phase>=2&remain_distance<=401&remain_distance>=399&order_rate<=40"
        data5= "is_finalcorner==1&order_rate>=40&order_rate<=75&lane_type==0"
        data6= "distance_rate>=66&order_rate_out50_continue==1&temptation_count==0"
        data7= "phase>=1&slope==2&order_rate>=50&order_rate<=80"
        data8= "distance_type==3&phase_laterhalf_random==1&order_rate<=50@distance_type==4&phase_laterhalf_random==1&order_rate<=50"
        data9= "distance_rate>=50&corner==0&order_rate>=70&order_rate<=75&is_overtake==1@distance_rate>=50&corner==0&order_rate<=30&order_rate>=20"
        data10= "phase>=2&corner!=0&order_rate>=65&order_rate<=70"
        make_condition_data(202342, 'condition_1', data1)
        make_condition_data(900251, 'condition_1', data2)
        make_condition_data(100091, 'condition_1', data3)
        make_condition_data(100471, 'condition_2', data4)
        make_condition_data(900361, 'precondition_1', data5)
        make_condition_data(202492, 'precondition_1', data6)
        make_condition_data(110081, 'precondition_2', data7)
        make_condition_data(900651, 'condition_2', data8)
        make_condition_data(100211, 'condition_1', data9)
        make_condition_data(900271, 'condition_1', data10)
    elif mode=="ability":
        make_ability_data(0, 0, 0, 0, 0, 0)
        make_ability_data(1, 2, 0, 2000, -2000, 0)
        make_ability_data(501, 502, 503, 10000, 20000, 30000)
        make_ability_data(13, 31, 6, 10000, 20000, 0)
    elif mode=="extract":
        extract_vars()
    elif mode=="order":
        extract_orders()
