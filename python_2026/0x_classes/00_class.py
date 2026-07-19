from typing import Generator

class person:
    def __init__(self, name: str = "", age: int = 0, height: float = 0.0) -> None:
        self.name: str = name
        self.age: int = age
        self.height: float = height

    # generator
    def get_person(self) -> Generator[str | int | float, None, None]:
        # About type
        """
            Yield type: str | int | float (because your generator yields all three)
            Send type: None
            Return type: None
        """
        yield self.name
        yield self.age
        yield self.height

    def produce_person(self, name: str, age: int, height: float) -> None:
        if name != self.name:
            self.name = name
        if age != self.age:
            self.age = age
        if height != self.height:
            self.height = height


p1: person = person("John Doe", 21, 5.9)            # object of class

print(type(p1))         # <class '__main__.person'>

# generator
g: Generator[str | int | float, None, None] = p1.get_person()
print(type(g))          # <class 'generator'>

print(next(g))
print(next(g))
print(next(g))


print(p1)           # <__main__.person object at 0x000002B80F458C20>            -- default object representation. 


# To change default object representation and want to more readable, add __str__ method:

# def __str__(self):
#     return f"Person(name={self.name}, age={self.age}, height={self.height})"
# print(p1)

# Output: Person(name=John Doe, age=21, height=5.9)