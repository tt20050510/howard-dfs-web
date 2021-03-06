import json


class BaseEmpty(object):
    def to_json(self) -> str:
        return json.dumps(self.super().__dict__, default=lambda o: {_: __ for _, __ in o.super().__dict__.items() if __ is not None},
                          ensure_ascii=False)

    def __str__(self):
        return self.super().__dict__.__str__()


    def to_dict(self) -> dict:
        return json.loads(
            json.dumps(super().__dict__, default=lambda o: {_: __ for _, __ in o.super().__dict__.items() if __ is not None},
                       ensure_ascii=False))
