def response_skill_data(data):
    response = []
    for i, d in enumerate(data):
        skill_id, rarity, group_id, skill_category, condition_1, condition_2, skill_name, skill_desc = d
        response.append(f'{i+1}. {skill_name} (희귀도: {rarity} / 분류: {skill_category})')
        response.append(f'설명: {skill_desc}')

        if condition_2 != "":
            response.append(f'조건1: {condition_1}')
            response.append(f'조건2: {condition_2}') 
        else:
            response.append(f'조건: {condition_1}')
            
        response.append('')

    return '\n'.join(response)
        