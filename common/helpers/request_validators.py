class PatchRequestValidator:
    def __init__(self):
        pass

    def validate(self, data):
        for k, v in data.items():
            if v == "":
                data[k] = None
        return data