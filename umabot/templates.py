def carousel_itemcard_template(simpletext, response, func, message=None):
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
            "quickReplies": func(message)
        }
    }

def itemcard_template(title, imageurl, response, buttons, func, texttitle=None, textdescription=None, message=None):
    return {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "itemCard": {
                        "profile": {
                            "title": title,
                            "imageUrl": imageurl
                        },
                        "itemList": response,
                        "buttons": buttons,
                        "title": texttitle,
                        "description": textdescription
                    }
                }
            ],
            "quickReplies": func(message)
        }
    }

def carousel_listcard_template(simpletext, response, func, message=None):
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
                        "type": "listCard",
                        "items": response
                    }
                }
            ],
            "quickReplies": func(message)
        }
    }

def listcard_template(title, imageurl, response, func, message=None):
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
            "quickReplies": func(message)
        }
    }

def textcard_template(title, description, buttons, func, message=None):
    return {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "textCard": {
                        "title": title,
                        "description": description,
                        "buttons": buttons
                    }
                }
            ],
            "quickReplies": func(message)
        }
    }

def simpletext_template(text, func, message=None):
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
            "quickReplies": func(message)
        }
    }

def quick_skill_replies_list(message=None):
    return [
        {
            "label": "다른 스킬",
            "action": "message",
            "messageText": "스킬"
        },
        {
            "label": "캐릭터",
            "action": "message",
            "messageText": "캐릭터"
        },
        {
            "label": "서포트",
            "action": "message",
            "messageText": "서포트 카드"
        },
        {
            "label": "초기메뉴",
            "action": "message",
            "messageText": "초기메뉴"
        }
    ]

def quick_chara_replies_list(message=None):
    return [
        {
            "label": "다른 캐릭터",
            "action": "message",
            "messageText": "캐릭터"
        },
        {
            "label": "서포트",
            "action": "message",
            "messageText": "서포트 카드"
        },
        {
            "label": "스킬",
            "action": "message",
            "messageText": "스킬"
        },
        {
            "label": "초기메뉴",
            "action": "message",
            "messageText": "초기메뉴"
        }
    ]

def quick_support_replies_list(message=None):
    return [
        {
            "label": "다른 서포트",
            "action": "message",
            "messageText": "서포트 카드"
        },
        {
            "label": "캐릭터",
            "action": "message",
            "messageText": "캐릭터"
        },
        {
            "label": "스킬",
            "action": "message",
            "messageText": "스킬"
        },
        {
            "label": "초기메뉴",
            "action": "message",
            "messageText": "초기메뉴"
        }
    ]

def quick_empty_list(message=None):
    return [
    ]