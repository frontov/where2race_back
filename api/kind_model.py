class KindModel:
    name = None
    title = None

    def __init__(self, name, title):
        self.name = name
        self.title = title


def to_models(d: dict[str, str]):
    result = []
    for k, v in d.items():
        result.append(KindModel(k, v))

    return result
