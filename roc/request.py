import uuid


class Request:
    def __init__(self, path: str, params: dict, key: int | str | None = None):
        self.path: str = path
        self.params: dict = params
        if key is None:
            key = uuid.uuid4().hex

        self.id: int | str = key

    def get_path(self) -> str:
        return self.path

    def get_params(self) -> dict:
        return self.params

    def get_id(self) -> int | str:
        return self.id


class Response:
    def __init__(self, key: int | str | None, result: dict | None, error: dict | None):
        self.id: int | str | None = key
        self.result: dict | None = result
        self.error: dict | None = error

    def get_id(self) -> int | str | None:
        return self.id

    def get_result(self) -> dict | None:
        return self.result

    def get_error(self) -> dict | None:
        return self.error


def make_response(data: dict) -> Response:
    for key in ["id", "result", "error"]:
        if key not in data:
            data[key] = None

    return Response(data["id"], data["result"], data["error"])
