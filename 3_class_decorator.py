"""
Scenario 3: Class Decorator
Description:
You're building a singleton pattern implementation to ensure that a class has only one instance. 
Create a class decorator that ensures only one instance of a class is created.
"""

from functools import wraps 

def singleton(cls):
    instance = dict()
    @wraps(cls)
    def get_instance(*args,**kwargs):
        if cls not in instance:
            instance[cls] = cls(*args,**kwargs)
        return instance[cls]
    return get_instance

@singleton
class Pet:
    def __init__(self,name,age) -> None:
        self.name = name
        self.age = age
        print("I am invoked")

    def __str__(self) -> str:
        return f"Name:{self.name} Age:{self.age}"

pet1 = Pet("Rocky",3)
print(pet1, "id:",id(pet1))
pet2 = Pet("Mini",7)
print(pet2,"id:",id(pet2))