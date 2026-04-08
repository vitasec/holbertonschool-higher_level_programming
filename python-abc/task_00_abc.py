#!/usr/bin/python3
from abc import ABC, abstractmethod
"""import necessary components from abc"""


class Animal(ABC):
    """abstract class that define  animal"""
    @abstractmethod
    def sound(self):
        pass

    
class Dog(Animal):
    def sound(self): 
        return "Bark"

class Cat(Animal):
    def sound(self):
        return "Meow"
