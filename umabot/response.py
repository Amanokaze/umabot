import os
from templates import carousel_itemcard_template, simpletext_template
from utils import make_condition_data

def response_skill_data(data):
    limit_count = 5
    simpletext = str()

    # data is changed to dataframe, so code will be changed
    if len(data) > limit_count:
        simpletext = f'검색 결과가 {limit_count}개가 넘습니다. 처음 검색된 {limit_count}개만 표시합니다.'
    elif len(data) == 0:
        simpletext = '검색 결과가 없습니다.'
    else:
        simpletext = f'전체 {len(data)}개의 검색 결과가 있습니다.'
    
    response = []
    for i, r in data.iterrows():
        if i >= limit_count:
            break

        response_item = dict()
        response_item["itemList"] = list()
        response_item["itemListAlignment"] = "left"

        response_item["buttons"] = [{"label": "조건", "action": "block", "blockId": f"65a9379b4d97486c0d142ff7", "extra": {"skill_id": r["skill_id"]}}]
        response_item["buttonLayout"] = "vertical"

        response_item["imageTitle"] = {
            "imageUrl": f"https://gametora.com/images/umamusume/skill_icons/utx_ico_skill_{r['icon_id']}.png",
            "title": f"{r['skill_name']}"
        }

        if r['need_skill_point'] > 1:
            response_item["title"] = f"{round(r['need_skill_point'])}Pt"
        else:
            response_item["title"] = "고유기"

        response_item["description"] = r["skill_desc"].replace("\\n", " ")

        ability = f"{r['ability_type_1_1']}{'상승' if r['float_ability_value_1_1'] > 0 else '감소'} {r['float_ability_value_1_1']/10000}"
        if r["ability_type_1_2"] > 0:
            ability = ability + " / " + f"{r['ability_type_1_2']}{'상승' if r['float_ability_value_1_2'] > 0 else '감소'} {r['float_ability_value_1_2']/10000}"
        if r["ability_type_1_3"] > 0:
            ability = ability + " / " + f"{r['ability_type_1_3']}{'상승' if r['float_ability_value_1_3'] > 0 else '감소'} {r['float_ability_value_1_3']/10000}"

        condition = str()
        if r["precondition_1"]:
            condition = make_condition_data(r["precondition_1"])
        if r["condition_1"]:
            condition = condition + " " + make_condition_data(r["condition_1"])

        response_item["itemList"].append({"title": "조건", "description": condition})
        response_item["itemList"].append({"title": "효과", "description": ability})
        response_item["itemList"].append({"title": "지속/쿨", "description": f"{r['float_ability_time_1']/10000}초 / {r['float_cooldown_time_1']/10000}초"})

        response.append(response_item)

    return carousel_itemcard_template(simpletext, response)

def response_skill_condition_data(data):
    response_data = data.iloc[0]
    id, pc1, c1, pc2, c2 = response_data
    pc1_data = make_condition_data(pc1)
    pc2_data = make_condition_data(pc2)
    c1_data = make_condition_data(c1)
    c2_data = make_condition_data(c2)

    simpletext = str()
    simpletext_list = []
    if c2 is None or c2 == "":
        simpletext_list.append('조건')
        if pc1:
            simpletext_list.append(pc1_data)
        if c1:
            simpletext_list.append(c1_data)

        simpletext = "\n".join(simpletext_list)

    else:
        simpletext_list.append('조건1')
        if pc1:
            simpletext_list.append(pc1_data)
        if c1:
            simpletext_list.append(c1_data)

        simpletext_list.append('')
        simpletext_list.append('조건2')
        if pc2:
            simpletext_list.append(pc2_data)
        if c2:
            simpletext_list.append(c2_data)

        simpletext = "\n".join(simpletext_list)

    return simpletext_template(simpletext)
