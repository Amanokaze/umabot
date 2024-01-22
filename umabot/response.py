import os
from templates import carousel_itemcard_template, simpletext_template, quick_skill_replies_list, quick_chara_replies_list
from utils import make_condition_data, make_ability_data

grade_for_str = {
    1: "G",
    2: "F",
    3: "E",
    4: "D",
    5: "C",
    6: "B",
    7: "A",
    8: "S"
}

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

        ability = make_ability_data(r["ability_type_1_1"], r["ability_type_1_2"], r["ability_type_1_3"], r["float_ability_value_1_1"], r["float_ability_value_1_2"], r["float_ability_value_1_3"])

        condition = str()
        if r["precondition_1"]:
            condition = make_condition_data(r["skill_id"], "precondition_1", r["precondition_1"])
        if r["condition_1"]:
            condition = condition + " " + make_condition_data(r["skill_id"], "condition_1", r["condition_1"])
        
        condition = condition.strip()

        response_item["itemList"].append({"title": "조건", "description": condition})
        response_item["itemList"].append({"title": "효과", "description": ability})
        response_item["itemList"].append({"title": "지속/쿨", "description": f"{r['float_ability_time_1']/10000}초 / {r['float_cooldown_time_1']/10000}초"})

        response.append(response_item)

    return carousel_itemcard_template(simpletext, response, quick_skill_replies_list)

def response_skill_condition_data(data):
    response_data = data.iloc[0]
    id, pc1, c1, pc2, c2, at11, at12, at13, at21, at22, at23, av11, av12, av13, av21, av22, av23 = response_data
    pc1_data = make_condition_data(id, "precondition_1", pc1)
    pc2_data = make_condition_data(id, "precondition_2", pc2)
    c1_data = make_condition_data(id, "condition_1", c1)
    c2_data = make_condition_data(id, "condition_2", c2)

    simpletext = str()
    simpletext_list = []
    if c2 is None or c2 == "":
        if pc1:
            simpletext_list.append('전제조건')
            simpletext_list.append(pc1_data)
        if c1:
            simpletext_list.append('조건')
            simpletext_list.append(c1_data)

        simpletext_list.append('효과')
        simpletext_list.append(make_ability_data(at11, at12, at13, av11, av12, av13))

        simpletext = "\n".join(simpletext_list)

    else:
        if pc1:
            simpletext_list.append('전제조건1')
            simpletext_list.append(pc1_data)
        if c1:
            simpletext_list.append('조건1')
            simpletext_list.append(c1_data)

        simpletext_list.append('효과')
        simpletext_list.append(make_ability_data(at11, at12, at13, av11, av12, av13))

        simpletext_list.append('')
        
        if pc2:
            simpletext_list.append('전제조건2')
            simpletext_list.append(pc2_data)
        if c2:
            simpletext_list.append('조건2')
            simpletext_list.append(c2_data)

        simpletext_list.append('효과')
        simpletext_list.append(make_ability_data(at21, at22, at23, av21, av22, av23))

        simpletext = "\n".join(simpletext_list)

    return simpletext_template(simpletext, quick_skill_replies_list)

def response_card_data(data):
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

        response_item["buttons"] = [{"label": "더보기", "action": "block", "blockId": f"65ae13b211d6d30690c758d6", "extra": {"card_id": r["card_id"]}}]
        response_item["buttonLayout"] = "vertical"

        response_item["imageTitle"] = {
            "imageUrl": f"https://gametora.com/images/umamusume/characters/chara_stand_{r['chara_id']}_{r['card_id']}.png",
            "title": f"{r['card_name']}{r['chara_name']}"
        }

        response_item["itemList"].append({"title": "출시일자", "description": r["start_date"] if r["start_date"] not in ("2017-01-01", "2016-12-31") else "2022-06-20"})
        response_item["itemList"].append({"title": "능력치 상승", "description": f"{r['talent_speed']}% / {r['talent_stamina']}% / {r['talent_pow']}% / {r['talent_guts']}% / {r['talent_wiz']}%"})
        response_item["itemList"].append({"title": "경기장 적성", "description": f"{grade_for_str[r['proper_ground_turf']]} / {grade_for_str[r['proper_ground_dirt']]}"})
        response_item["itemList"].append({"title": "거리 적성", "description": f"{grade_for_str[r['proper_distance_short']]} / {grade_for_str[r['proper_distance_mile']]} / {grade_for_str[r['proper_distance_middle']]} / {grade_for_str[r['proper_distance_long']]}"})
        response_item["itemList"].append({"title": "각질 적성", "description": f"{grade_for_str[r['proper_running_style_nige']]} / {grade_for_str[r['proper_running_style_senko']]} / {grade_for_str[r['proper_running_style_sashi']]} / {grade_for_str[r['proper_running_style_oikomi']]}"})

        response.append(response_item)

    return carousel_itemcard_template(simpletext, response, quick_chara_replies_list)
