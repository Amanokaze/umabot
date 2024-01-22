def carousel_itemcard_template(simpletext, response, func):
    return {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": simpletext
                    }
                },
                {
                    "carousel": {
                        "type": "itemCard",
                        "items": response
                    }
                }
            ],
            "quickReplies": func()
        }
    }

def simpletext_template(text, func):
    return {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": text
                    }
                }
            ],
            "quickReplies": func()
        }
    }

def quick_skill_replies_list():
    return [
        {
            "label": "스킬",
            "action": "message",
            "messageText": "스킬"
        },
        {
            "label": "캐릭터",
            "action": "message",
            "messageText": "캐릭터"
        },
        {
            "label": "초기메뉴",
            "action": "message",
            "messageText": "업데이트 예정"
        }
    ]

def quick_chara_replies_list():
    return [
        {
            "label": "고유기",
            "action": "message",
            "messageText": "고유기"
        },
        {
            "label": "초기 스킬",
            "action": "message",
            "messageText": "초기 스킬"
        },
        {
            "label": "각성 스킬",
            "action": "message",
            "messageText": "각성 스킬"
        },
        {
            "label": "이벤트",
            "action": "message",
            "messageText": "이벤트"
        },
        {
            "label": "다른 캐릭터",
            "action": "message",
            "messageText": "캐릭터"
        },
        {
            "label": "초기메뉴",
            "action": "message",
            "messageText": "업데이트 예정"
        }
    ]