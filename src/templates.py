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
            ]
        }
    }
    
