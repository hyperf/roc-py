from roc.request import Request
import json


class DataFormatter:
    def format_request(self, request: Request) -> str:
        return json.dumps({
            "id": request.get_id(),
            "path": request.get_path(),
            "data": request.get_params(),
        })
