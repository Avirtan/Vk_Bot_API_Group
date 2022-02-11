import json

class HandlerJson:

    @staticmethod
    def json_to_dict(strJson:str):
        return json.loads(strJson)