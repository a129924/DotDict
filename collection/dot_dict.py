from .custom_types import KeyType, ValueType

class DotDict(dict):
    def __init__(self, *args, **kwargs)->None:
        super(DotDict, self).__init__(*args, **kwargs)
        for key, value in self.items():
            if isinstance(value, dict):
                self[key] = DotDict(value)

    def __getitem__(self, key: KeyType)->ValueType:
        if key not in self:
            self[key] = DotDict()
        return super(DotDict, self).__getitem__(key)

    def __setitem__(self, key: KeyType, value: ValueType)->None:
        if isinstance(value, dict):
            value = DotDict(value)
        super(DotDict, self).__setitem__(key, value)
