class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class TestClass(metaclass = Singleton):
    def __init__(self, name = 'first', value = 12):
        self.name = name
        self.value = value