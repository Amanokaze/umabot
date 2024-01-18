import os
from templates import response_template

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

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

        response_item["itemList"].append({"title": "조건", "description": f"{r['precondition_1']}f{' ' if r['precondition_1'] else ''}{r['condition_1']}"})
        response_item["itemList"].append({"title": "효과", "description": ability})
        response_item["itemList"].append({"title": "지속/쿨", "description": f"{r['float_ability_time_1']/10000}초 / {r['float_cooldown_time_1']/10000}초"})

        response.append(response_item)

    return response_template(simpletext, response)
        