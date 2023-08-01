from abc import ABC, abstractmethod
from enum import Enum, auto


class Gender(Enum):
    MALE = auto()
    FEMALE = auto()


class Animal(ABC):
    def __init__(self, name: str, age: int, gender: Gender):
        self.name = name
        self.age = age
        self.gender = gender

    @abstractmethod
    def wander(self):
        ...

    @abstractmethod
    def sleep(self):
        ...

    @abstractmethod
    def eat(self):
        ...

    def __str__(self):
        return f'{self.__class__.__name__}(name = {self.name}, age = {self.age}, gender = {self.gender})'

    def __repr__(self):
        return self.__str__()
