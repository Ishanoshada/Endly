# endly/json.py
import json

class JsonResponse:
    @staticmethod
    def json_response(data, status=200):
        return json.dumps(data), status