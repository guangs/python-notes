from typing import Union


def say_hi(name: str) -> str:
    return f'Hi {name}'


greeting = say_hi(123)  # use tool mypy can find out this type error
print(greeting)


def add(x: Union[int, float], y: Union[int, float]) -> Union[int, float]:
    return x + y

'''
Starting from Python 3.10

def add(x: int | float, y: int | float) -> int | float:
    return x + y

'''

# typing aliases
number = Union[int, float]

def add(x: number, y: number) -> number:
    return x + y


# List
from typing import List
ratings: List[int] = [1, 2, 3]


# None
def log(message: str) -> None:
    print(message)
