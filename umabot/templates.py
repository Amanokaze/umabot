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

def itemcard_template(title, imageurl, response, func):
    return {
        "profile": {
            "title": title,
            "imageUrl": imageurl,
        },
        "itemList": response,
        "buttons": [
            {
                "action": "message",
                "label": "상세정보",
                "messageText": title
            }
        ]
    }

def listcard_template(title, imageurl, response, func):
    return {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "listCard": {
                        "header": {
                            "title": title,
                            "imageUrl": imageurl
                        },
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
            "messageText": "초기메뉴"
        }
    ]

def quick_chara_replies_list():
    return [
        {
            "label": "다른 캐릭터",
            "action": "message",
            "messageText": "캐릭터"
        },
        {
            "label": "초기메뉴",
            "action": "message",
            "messageText": "초기메뉴"
        }
    ]

def quick_chara_detail_replies_list(name):
    return [
        {
            "label": "캐릭터 메인",
            "action": "block",
            "blockId": "65a794a2c704e241fe14e756",
            "messageText": name,
            "extra": {
                "name": name
            }
        },
        {
            "label": "다른 캐릭터",
            "action": "message",
            "messageText": "캐릭터"
        },
        {
            "label": "초기메뉴",
            "action": "message",
            "messageText": "초기메뉴"
        }
    ]