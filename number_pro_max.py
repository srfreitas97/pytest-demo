class NumberProMax():
    def __init__(self, value: float) -> None:
        self.value = value
    def is_odd(self):
        return self.value % 2
    def is_greater_than(self, number: float):
        return self.value > number