class Calculator:
    def __init__(self) -> None:
        self.history = []

    def add(self, a: int, b: int) -> int:
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result

    def sub(self, a: int, b: int) -> int:
        result = a - b
        self.history.append(f"{a} - {b} = {result}")
        return result

    def mul(self, a: int, b: int) -> int:
        result = a * b
        self.history.append(f"{a} * {b} = {result}")
        return result

    def div(self, a: int, b: int) -> int:
        if b == 0:
            raise ZeroDivisionError

        result = a / b
        self.history.append(f"{a} / {b} = {result}")
        return int(result)

    def pow(self, a: int, b: int) -> int:
        result = a**b
        self.history.append(f"{a} ** {b} = {result}")
        return result
