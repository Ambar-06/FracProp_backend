def get_response_or_error(response: dict) -> tuple:
    response_keys = ["response_data", "errors"]
    resp = None
    code = None
    for key, value in response.items():
        if key in response_keys:
            resp = value
        else:
            code = value
    return resp, code
