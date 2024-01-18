import os
from templates import response_template

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def response_skill_data(data):
    limit_count = 5
    simpletext = str()

    if len(data) > limit_count:
        simpletext = f'검색 결과가 {limit_count}개가 넘습니다. 처음 검색된 {limit_count}개만 표시합니다.'
    elif len(data) == 0:
        simpletext = '검색 결과가 없습니다.'
    else:
        simpletext = f'전체 {len(data)}개의 검색 결과가 있습니다.'
    
    response = []
    for i, d in enumerate(data):
        if i >= limit_count:
            break

        response_item = dict()
        response_item["itemList"] = list()
        response_item["itemListAlignment"] = "left"

        skill_id, rarity, group_id, icon_id, skill_category, condition_1, condition_2, skill_name, skill_desc = d

        response_item["imageTitle"] = {
            "imageUrl": f"https://gametora.com/images/umamusume/skill_icons/utx_ico_skill_{icon_id}.png",
            "title": skill_name
        }

        response_item["itemList"].append({
            "title": "설명",
            "description": skill_desc.replace('\\n', ' ')
        })

        if condition_2 != "":
            response_item["itemList"].append({
                "title": "조건1",
                "description": condition_1
            })
            response_item["itemList"].append({
                "title": "조건2",
                "description": condition_2
            })
        else:
            response_item["itemList"].append({
                "title": "조건",
                "description": condition_1
            })

        # 이미지 표시만 되면 저거 다 없애버려도 되는데...
        response_item["itemList"].append({
            "title": "희귀도",
            "description": rarity
        })
        response_item["itemList"].append({
            "title": "분류",
            "description": skill_category
        })

        response.append(response_item)

    return response_template(simpletext, response)
        