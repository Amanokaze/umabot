def carousel_itemcard_template(simpletext, response):
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
            "quickReplies": quickreplies_list()
        }
    }

def simpletext_template(text):
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
            "quickReplies": quickreplies_list()
        }
    }

def quickreplies_list():
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
            "label": "업데이트 예정",
            "action": "message",
            "messageText": "업데이트 예정"
        }
    ]
