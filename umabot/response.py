import os
import templates as tpl 
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

    return tpl.carousel_itemcard_template(simpletext, response, tpl.quick_skill_replies_list)

def response_skill_condition_data(data, quick_type):
    response_data = data.iloc[0]
    id, name, pc1, c1, pc2, c2, at11, at12, at13, at21, at22, at23, av11, av12, av13, av21, av22, av23 = response_data
    pc1_data = make_condition_data(id, "precondition_1", pc1)
    pc2_data = make_condition_data(id, "precondition_2", pc2)
    c1_data = make_condition_data(id, "condition_1", c1)
    c2_data = make_condition_data(id, "condition_2", c2)

    title = name
    description = str()
    desc_list = []
    if c2 is None or c2 == "":
        if pc1:
            desc_list.append('전제조건')
            desc_list.append(pc1_data)
        if c1:
            desc_list.append('조건')
            desc_list.append(c1_data)

        desc_list.append('효과')
        desc_list.append(make_ability_data(at11, at12, at13, av11, av12, av13))

        description = "\n".join(desc_list)

    else:
        if pc1:
            desc_list.append('전제조건1')
            desc_list.append(pc1_data)
        if c1:
            desc_list.append('조건1')
            desc_list.append(c1_data)

        desc_list.append('효과')
        desc_list.append(make_ability_data(at11, at12, at13, av11, av12, av13))

        desc_list.append('')
        
        if pc2:
            desc_list.append('전제조건2')
            desc_list.append(pc2_data)
        if c2:
            desc_list.append('조건2')
            desc_list.append(c2_data)

        desc_list.append('효과')
        desc_list.append(make_ability_data(at21, at22, at23, av21, av22, av23))

        description = "\n".join(desc_list)

    buttons = []

    return_func = None
    if quick_type == 0:
        return_func = tpl.quick_skill_replies_list
    elif quick_type == 1:
        return_func = tpl.quick_chara_replies_list
    else:
        return_func = tpl.quick_skill_replies_list

    return tpl.textcard_template(title, description, buttons, return_func)

def response_skill_unique_card_data(data):
    card_data = data.iloc[0]

    response = []    
    buttons = [{"label": "조건", "action": "block", "blockId": f"65a9379b4d97486c0d142ff7", "extra": {"skill_id": f"{card_data['skill_id']}", "quick_type": "1"}}]
    title = f"{card_data['skill_name']}"
    imageurl = f"https://gametora.com/images/umamusume/skill_icons/utx_ico_skill_{card_data['icon_id']}.png"

    ability = make_ability_data(card_data["ability_type_1_1"], card_data["ability_type_1_2"], card_data["ability_type_1_3"], card_data["float_ability_value_1_1"], card_data["float_ability_value_1_2"], card_data["float_ability_value_1_3"])

    condition = str()
    if card_data["precondition_1"]:
        condition = make_condition_data(card_data["skill_id"], "precondition_1", card_data["precondition_1"])
    if card_data["condition_1"]:
        condition = condition + " " + make_condition_data(card_data["skill_id"], "condition_1", card_data["condition_1"])
    
    condition = condition.strip()

    response.append({"title": "조건", "description": condition})
    response.append({"title": "효과", "description": ability})
    response.append({"title": "지속/쿨", "description": f"{card_data['float_ability_time_1']/10000}초 / {card_data['float_cooldown_time_1']/10000}초"})

    return tpl.itemcard_template(title, imageurl, response, buttons, tpl.quick_chara_replies_list)

def response_card_data(data):
    limit_count = 5
    simpletext = str()

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

    return tpl.carousel_itemcard_template(simpletext, response, tpl.quick_chara_replies_list)

def response_card_detail_data(data):
    response_data = data.iloc[0]
    id, chara_id, available_skill_set_id, skill_set, speed, stamina, pow, guts, wiz, card_name, chara_name, unique_skill_id, unique_skill_name, unique_skill_icon_id = response_data
    title = f"{card_name}{chara_name}"
    imageurl = f"https://gametora.com/images/umamusume/characters/chara_stand_{'chara_id'}_{id}.png"
    
    response = []
    response.append({
        "title": "기본 능력치",
        "description": f"{speed} / {stamina} / {pow} / {guts} / {wiz} (3성 기준)",
        "imageUrl": "https://i.imgur.com/aF6VtSy.png",
        "action": "block",
        "blockId": "65ae13c5c4a3c1384a4c6646",
        "extra": { "card_id": f"{id}" }
    })
    response.append({
        "title": "고유기",
        "description": unique_skill_name,
        "imageUrl": f"https://gametora.com/images/umamusume/skill_icons/utx_ico_skill_{unique_skill_icon_id}.png",
        "action": "block",
        "blockId": "65adee5b8f90320133173b99",
        "extra": { "skill_id": f"{unique_skill_id}"}
    })
    response.append({
        "title": "초기 스킬",
        "imageUrl": "https://gametora.com/images/umamusume/skill_icons/utx_ico_skill_10011.png",
        "action": "block",
        "blockId": "65adee6210c91b797bc94716",
        "extra": { "available_skill_set_id": f"{available_skill_set_id}"}
    })
    response.append({
        "title": "각성 스킬",
        "imageUrl": "https://gametora.com/images/umamusume/skill_icons/utx_ico_skill_20011.png",
        "action": "block",
        "blockId": "65adee6843855575ff73b340",
        "extra": { "available_skill_set_id": f"{available_skill_set_id}"}
    })
    response.append({
        "title": "이벤트",
        "description": "추후 구현 예정",
        "imageUrl": "https://i.imgur.com/dtQFkJf.png",    
    })

    return tpl.listcard_template(title, imageurl, response, tpl.quick_chara_replies_list)