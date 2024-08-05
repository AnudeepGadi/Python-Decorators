"""
Scenario: Parameterized Decorator
Description:
You're building an access control system for an API. 
Create a parameterized decorator that takes a user role as an argument and 
checks if the user has the necessary permissions to execute the function. 
If the user does not have the required role, the function should not execute
and an appropriate message should be returned.
"""
from functools import wraps
from typing import List

def role_verify_decorator(roles:List[str]):
    def wrapper(func):
        @wraps(func)
        def inner(*args,**kwargs):
            if kwargs["current_user"]["role"] in roles:
                return func(*args,**kwargs)
            else:
                return "You do not have necessary permissions"
        return inner
    return wrapper


@role_verify_decorator(roles=["admin"])
def create_user(current_user,name,age):
    """
    Equivalent to create_user = role_verify_decorator(roles=["admin"])(create_user) 
    """
    return(f"Creating user {name} {age}")


@role_verify_decorator(roles=["admin","user"])
def read_user(current_user):
    """
    Equivalent to create_user = role_verify_decorator(roles=["admin,"user"])(create_user) 
    """
    return("Printing user details")


print(create_user(current_user={"role":"admin"},name="Ram",age="26")) #Output: Creating user Ram 26
print(create_user(current_user={"role":"user"},name="Krish",age="26")) #Output: You dont have permission
print(read_user(current_user={"role":"user"})) #Output: Printing user details
print(read_user(current_user={"role":"admin"})) #Output: Printing user details
