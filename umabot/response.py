import os
import templates as tpl 
import utils 

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

support_grade_for_str = {
    3: "SSR",
    2: "SR",
    1: "R"
}

skill_category_for_str = {
    0: "패시브 스킬",
    1: "초반 발동 스킬",
    2: "중반 발동 스킬",
    3: "종반 발동 스킬",
    4: "상시 발동 스킬",
    5: "고유기/계승기",
    101: "카니발 보너스"

}

def response_skill_data(data):
    limit_count = 5
    simpletext = str()

    # data is changed to dataframe, so code will be changed
    if len(data) == 0:
        title = '스킬 검색 결과 없음'
        description = '검색 결과가 없습니다. 다시 검색하시겠습니까?'
        buttons = [
            {"label": "다시 검색", "action": "message", "messageText": "스킬"},
            {"label": "초기메뉴", "action": "message", "messageText": "초기메뉴"}
        ]

        return tpl.textcard_template(title, description, buttons, tpl.quick_empty_list)
    
    elif len(data) > limit_count:
        simpletext = f'검색 결과가 {limit_count}개가 넘습니다. 처음 검색된 {limit_count}개만 표시합니다.'
    else:
        simpletext = f'전체 {len(data)}개의 검색 결과가 있습니다.'
    
    response = []
    for i, r in data.iterrows():
        if i >= limit_count:
            break

        response_item = dict()
        response_item["itemList"] = list()
        response_item["itemListAlignment"] = "left"

        response_item["buttons"] = [
            {"label": "조건", "action": "block", "blockId": f"65a9379b4d97486c0d142ff7", "extra": {"skill_id": r["skill_id"]}},
            {"label": "보유 카드", "action": "block", "blockId": f"65af6c9b6757d91c3fcb23fe", "extra": {"skill_id": r["skill_id"]}},
        ]
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

        ability = utils.make_ability_data(r["ability_type_1_1"], r["ability_type_1_2"], r["ability_type_1_3"], r["float_ability_value_1_1"], r["float_ability_value_1_2"], r["float_ability_value_1_3"])

        condition = str()
        if r["precondition_1"]:
            condition = utils.make_condition_data(r["skill_id"], "precondition_1", r["precondition_1"])
        if r["condition_1"]:
            condition = condition + " " + utils.make_condition_data(r["skill_id"], "condition_1", r["condition_1"])
        
        condition = condition.strip()

        response_item["itemList"].append({"title": "조건", "description": condition})
        response_item["itemList"].append({"title": "효과", "description": ability})
        response_item["itemList"].append({"title": "지속/쿨", "description": f"{r['float_ability_time_1']/10000}초 / {r['float_cooldown_time_1']/10000}초"})

        response.append(response_item)

    return tpl.carousel_itemcard_template(simpletext, response, tpl.quick_skill_replies_list)

def response_skill_condition_data(data, quick_type):
    response_data = data.iloc[0]
    id, name, pc1, c1, pc2, c2, at11, at12, at13, at21, at22, at23, av11, av12, av13, av21, av22, av23 = response_data
    pc1_data = utils.make_condition_data(id, "precondition_1", pc1)
    pc2_data = utils.make_condition_data(id, "precondition_2", pc2)
    c1_data = utils.make_condition_data(id, "condition_1", c1)
    c2_data = utils.make_condition_data(id, "condition_2", c2)

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
        desc_list.append(utils.make_ability_data(at11, at12, at13, av11, av12, av13))

        description = "\n".join(desc_list)

    else:
        if pc1:
            desc_list.append('전제조건1')
            desc_list.append(pc1_data)
        if c1:
            desc_list.append('조건1')
            desc_list.append(c1_data)

        desc_list.append('효과')
        desc_list.append(utils.make_ability_data(at11, at12, at13, av11, av12, av13))

        desc_list.append('')
        
        if pc2:
            desc_list.append('전제조건2')
            desc_list.append(pc2_data)
        if c2:
            desc_list.append('조건2')
            desc_list.append(c2_data)

        desc_list.append('효과')
        desc_list.append(utils.make_ability_data(at21, at22, at23, av21, av22, av23))

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

def response_skill_single_data(data, ref):
    if len(data) == 0:
        title = '잘못된 데이터'
        description = '입력 경로가 잘못되었습니다. 초기 메뉴로 이동합니다.'
        buttons = [
            {"label": "초기메뉴", "action": "message", "messageText": "초기메뉴"}
        ]

        return tpl.textcard_template(title, description, buttons, tpl.quick_empty_list)

    card_data = data.iloc[0]

    response = []    
    buttons = [
        {"label": "조건", "action": "block", "blockId": f"65a9379b4d97486c0d142ff7", "extra": {"skill_id": f"{card_data['skill_id']}", "ref": ref}},
        {"label": "보유 카드", "action": "block", "blockId": f"65af6c9b6757d91c3fcb23fe", "extra": {"skill_id": f"{card_data['skill_id']}"}}
    ]
    title = f"{card_data['skill_name']}"
    imageurl = f"https://gametora.com/images/umamusume/skill_icons/utx_ico_skill_{card_data['icon_id']}.png"

    ability = utils.make_ability_data(card_data["ability_type_1_1"], card_data["ability_type_1_2"], card_data["ability_type_1_3"], card_data["float_ability_value_1_1"], card_data["float_ability_value_1_2"], card_data["float_ability_value_1_3"])

    condition = str()
    if card_data["precondition_1"]:
        condition = utils.make_condition_data(card_data["skill_id"], "precondition_1", card_data["precondition_1"])
    if card_data["condition_1"]:
        condition = condition + " " + utils.make_condition_data(card_data["skill_id"], "condition_1", card_data["condition_1"])
    
    condition = condition.strip()

    response.append({"title": "조건", "description": condition})
    response.append({"title": "효과", "description": ability})
    response.append({"title": "지속/쿨", "description": f"{card_data['float_ability_time_1']/10000}초 / {card_data['float_cooldown_time_1']/10000}초"})

    texttitle = str()
    textdescription = str()
    if card_data['need_skill_point'] != None and card_data['need_skill_point'] > 1:
        texttitle = f"{round(card_data['need_skill_point'])}Pt"
        textdescription = card_data["skill_desc"].replace("\\n", " ")

    quickreply_func = None
    if ref == "support_card":
        quickreply_func = tpl.quick_support_replies_list
    elif ref == "character_card":
        quickreply_func = tpl.quick_chara_replies_list
    else:
        quickreply_func = tpl.quick_skill_replies_list

    return tpl.itemcard_template(title, imageurl, response, buttons, quickreply_func, texttitle, textdescription)

def response_skill_extra_card_data(data, flag):
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

        response_item["buttons"] = [{"label": "조건", "action": "block", "blockId": f"65a9379b4d97486c0d142ff7", "extra": {"skill_id": r["skill_id"], "quick_type": "1"}}]
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

        ability = utils.make_ability_data(r["ability_type_1_1"], r["ability_type_1_2"], r["ability_type_1_3"], r["float_ability_value_1_1"], r["float_ability_value_1_2"], r["float_ability_value_1_3"])

        condition = str()
        if r["precondition_1"]:
            condition = utils.make_condition_data(r["skill_id"], "precondition_1", r["precondition_1"])
        if r["condition_1"]:
            condition = condition + " " + utils.make_condition_data(r["skill_id"], "condition_1", r["condition_1"])
        
        condition = condition.strip()

        if flag:
            response_item["itemList"].append({"title": "각성 Lv.", "description": r["need_rank"]})
        response_item["itemList"].append({"title": "조건", "description": condition})
        response_item["itemList"].append({"title": "효과", "description": ability})
        response_item["itemList"].append({"title": "지속/쿨", "description": f"{r['float_ability_time_1']/10000}초 / {r['float_cooldown_time_1']/10000}초"})

        response.append(response_item)

    return tpl.carousel_itemcard_template(simpletext, response, tpl.quick_chara_replies_list)

def response_card_data(data):
    limit_count = 5
    simpletext = str()

    if len(data) == 0:
        title = '캐릭터 검색 결과 없음'
        description = '검색 결과가 없습니다. 다시 검색하시겠습니까?'
        buttons = [
            {"label": "다시 검색", "action": "message", "messageText": "캐릭터"},
            {"label": "초기메뉴", "action": "message", "messageText": "초기메뉴"}
        ]

        return tpl.textcard_template(title, description, buttons, tpl.quick_empty_list)
    
    elif len(data) > limit_count:
        simpletext = f'검색 결과가 {limit_count}개가 넘습니다. 처음 검색된 {limit_count}개만 표시합니다.'
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

        response_item["itemList"].append({"title": "출시일자", "description": utils.get_revised_start_date(r["start_date"])})
        response_item["itemList"].append({"title": "능력치 상승", "description": f"{r['talent_speed']}% / {r['talent_stamina']}% / {r['talent_pow']}% / {r['talent_guts']}% / {r['talent_wiz']}%"})
        response_item["itemList"].append({"title": "경기장 적성", "description": f"{grade_for_str[r['proper_ground_turf']]} / {grade_for_str[r['proper_ground_dirt']]}"})
        response_item["itemList"].append({"title": "거리 적성", "description": f"{grade_for_str[r['proper_distance_short']]} / {grade_for_str[r['proper_distance_mile']]} / {grade_for_str[r['proper_distance_middle']]} / {grade_for_str[r['proper_distance_long']]}"})
        response_item["itemList"].append({"title": "각질 적성", "description": f"{grade_for_str[r['proper_running_style_nige']]} / {grade_for_str[r['proper_running_style_senko']]} / {grade_for_str[r['proper_running_style_sashi']]} / {grade_for_str[r['proper_running_style_oikomi']]}"})

        response.append(response_item)

    return tpl.carousel_itemcard_template(simpletext, response, tpl.quick_chara_replies_list)

def response_card_detail_data(data):
    rdata = data.iloc[0]
    title = f"{rdata['card_name']}{rdata['chara_name']}"
    imageurl = f"https://gametora.com/images/umamusume/characters/chara_stand_{rdata['chara_id']}_{rdata['card_id']}.png"
    
    response = []

    response.append({
        "title": "기본 능력치",
        "description": f"{rdata['speed']} / {rdata['stamina']} / {rdata['pow']} / {rdata['guts']} / {rdata['wiz']} (3성 기준)",
        "imageUrl": "https://i.imgur.com/aF6VtSy.png",
        "action": "block",
        "blockId": "65ae13c5c4a3c1384a4c6646",
        "extra": { "card_id": f"{rdata['card_id']}" }
    })
    response.append({
        "title": "고유기",
        "description": rdata['unique_skill_name'],
        "imageUrl": f"https://gametora.com/images/umamusume/skill_icons/utx_ico_skill_{rdata['unique_skill_icon_id']}.png",
        "action": "block",
        "blockId": "65adee5b8f90320133173b99",
        "extra": { "skill_id": f"{rdata['unique_skill_id']}", "ref": "character_card"}
    })
    response.append({
        "title": "초기 스킬",
        "imageUrl": "https://gametora.com/images/umamusume/skill_icons/utx_ico_skill_10011.png",
        "action": "block",
        "blockId": "65adee6210c91b797bc94716",
        "extra": { "available_skill_set_id": f"{rdata['available_skill_set_id']}"}
    })
    response.append({
        "title": "각성 스킬",
        "imageUrl": "https://gametora.com/images/umamusume/skill_icons/utx_ico_skill_20011.png",
        "action": "block",
        "blockId": "65adee6843855575ff73b340",
        "extra": { "available_skill_set_id": f"{rdata['available_skill_set_id']}"}
    })
    response.append({
        "title": "이벤트",
        "description": "추후 구현 예정",
        "imageUrl": "https://i.imgur.com/dtQFkJf.png",    
    })

    return tpl.listcard_template(title, imageurl, response, tpl.quick_chara_replies_list)

def response_card_stat_data(data):
    response = []
    response_head = data.iloc[0]
    title = f"{response_head['card_name']}{response_head['chara_name']}"

    response.append(f"능력치 상승: {response_head['talent_speed']}% / {response_head['talent_stamina']}% / {response_head['talent_pow']}% / {response_head['talent_guts']}% / {response_head['talent_wiz']}%")
    response.append(f"경기장 적성: {grade_for_str[response_head['proper_ground_turf']]} / {grade_for_str[response_head['proper_ground_dirt']]}")
    response.append(f"거리 적성: {grade_for_str[response_head['proper_distance_short']]} / {grade_for_str[response_head['proper_distance_mile']]} / {grade_for_str[response_head['proper_distance_middle']]} / {grade_for_str[response_head['proper_distance_long']]}")
    response.append(f"각질 적성: {grade_for_str[response_head['proper_running_style_nige']]} / {grade_for_str[response_head['proper_running_style_senko']]} / {grade_for_str[response_head['proper_running_style_sashi']]} / {grade_for_str[response_head['proper_running_style_oikomi']]}")
    response.append("")

    for _, r in data.iterrows():
        response.append(f"{r['rarity']}성 : {r['speed']} / {r['stamina']} / {r['pow']} / {r['guts']} / {r['wiz']}")

    description = "\n".join(response)
    buttons = []

    return tpl.textcard_template(title, description, buttons, tpl.quick_chara_replies_list)

def response_support_card_data(data):
    total_limit_count = 20
    listitem_limit_count = 4
    simpletext = str()

    if len(data) == 0:
        title = '서포트 카드 검색 결과 없음'
        description = '검색 결과가 없습니다. 다시 검색하시겠습니까?'
        buttons = [
            {"label": "다시 검색", "action": "message", "messageText": "서포트 카드"},
            {"label": "초기메뉴", "action": "message", "messageText": "초기메뉴"}
        ]

        return tpl.textcard_template(title, description, buttons, tpl.quick_empty_list)
    
    elif len(data) > total_limit_count:
        simpletext = f'검색 결과가 {total_limit_count}개가 넘습니다. 처음 검색된 {total_limit_count}개만 표시합니다.'
    else:
        simpletext = f'전체 {len(data)}개의 검색 결과가 있습니다.'    

    response = []
    rarity_data = utils.make_dbl_list(data, "rarity", listitem_limit_count)

    for r in rarity_data:
        response_item = dict()
        response_item["header"] = {"title": f"검색 결과 - {support_grade_for_str[r[0]['rarity']]}"}
        response_item["items"] = []

        for rr in r:
            response_item["items"].append({
                "title": f"{rr['sc_name']}{rr['chara_name']}",
                "description": f"출시일자: {utils.get_revised_start_date(rr['start_date'])}",
                "imageUrl": f"https://gametora.com/images/umamusume/supports/tex_support_card_{rr['scd_id']}.png",
                "action": "block",
                "blockId": "65b2eeb61ac159401a43e609",
                "extra": { "scd_id": f"{rr['scd_id']}" }
            })

        response.append(response_item)

    return tpl.carousel_listcard_template(simpletext, response, tpl.quick_support_replies_list)

def response_support_card_menu_data(data):
    rdata = data.iloc[0]
    title = f"{rdata['sc_name']}{rdata['chara_name']}"
    imageurl = f"https://gametora.com/images/umamusume/supports/tex_support_card_{rdata['scd_id']}.png"
    
    response = []

    effect_icon_id = utils.get_support_command_id(rdata['support_card_type'], rdata['command_id'])
    response.append({
        "title": "효과",
        "description": f"최대 레벨 기준",
        "imageUrl": f"https://gametora.com/images/umamusume/icons/utx_ico_obtain_{effect_icon_id}.png",
        "action": "block",
        "blockId": "65b2eec6ea8e4936a2c4c89c",
        "extra": { "scd_id": f"{rdata['scd_id']}" }
    })

    # 육성 스킬은 나중에 이벤트 하고나서 연동해야 할 것..
    response.append({
        "title": "육성 스킬",
        "description": "추후 구현 예정",
        "imageUrl": "https://gametora.com/images/umamusume/icons/notes_square.png",
        "action": "block",
        "blockId": "65b2ef3176fd254fabd67a1a",
        "extra": { "scd_id": f"{rdata['scd_id']}" }
    })

    response.append({
        "title": "힌트 스킬",
        "imageUrl": f"https://gametora.com/images/umamusume/skill_icons/utx_ico_skill_{rdata['hint_icon_id']}.png",
        "action": "block",
        "blockId": "65b2ef132f5e1808a9593b06",
        "extra": { "scd_id": f"{rdata['scd_id']}" }
    })

    response.append({
        "title": "이벤트",
        "description": "추후 구현 예정",
        "imageUrl": "https://i.imgur.com/dtQFkJf.png",    
    })

    return tpl.listcard_template(title, imageurl, response, tpl.quick_support_replies_list)

def response_support_card_hint_list_data(data):
    total_limit_count = 20
    listitem_limit_count = 4
    simpletext = str()

    if len(data) == 0:
        title = '잘못된 데이터'
        description = '입력 경로가 잘못되었습니다. 초기 메뉴로 이동합니다.'
        buttons = [
            {"label": "초기메뉴", "action": "message", "messageText": "초기메뉴"}
        ]

        return tpl.textcard_template(title, description, buttons, tpl.quick_empty_list)
    
    elif len(data) > total_limit_count:
        simpletext = f'검색 결과가 {total_limit_count}개가 넘습니다. 처음 검색된 {total_limit_count}개만 표시합니다.'
    else:
        simpletext = f'전체 {len(data)}개의 검색 결과가 있습니다.'    

    response = []
    category_data = utils.make_dbl_list(data, "skill_category", listitem_limit_count)

    for r in category_data:
        response_item = dict()
        response_item["header"] = {"title": f"검색 결과 - {skill_category_for_str[r[0]['skill_category']]}"}
        response_item["items"] = []

        for rr in r:
            response_item["items"].append({
                "title": rr['skill_name'],
                "description": rr['skill_desc'].replace('\\n', ' '),
                "imageUrl": f"https://gametora.com/images/umamusume/skill_icons/utx_ico_skill_{rr['hint_icon_id']}.png",
                "action": "block",
                "blockId": "65adee5b8f90320133173b99",
                "extra": { "skill_id": f"{rr['skill_id']}", "ref": "support_card" }
            })

        response.append(response_item)

    return tpl.carousel_listcard_template(simpletext, response, tpl.quick_support_replies_list)