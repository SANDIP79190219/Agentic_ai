from typing import TypedDict

class person(TypedDict):
    name: str
    age: int

new_person: person = {'name': 'sandip', 'age': 45}    


print(new_person)

