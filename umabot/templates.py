def response_template(simpletext, response):
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
            "quickReplies": [
                {
                    "label": "다른 스킬 검색",
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
        }
    }
    
