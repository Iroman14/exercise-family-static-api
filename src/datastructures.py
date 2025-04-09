from random import randint

class Family:
    def __init__(self, last_name):
        self.last_name = last_name
        self._members = [
            {
                "id": self._generateId(),
                "first_name":"John",
                "last_name": self.last_name,
                "age": 33,
                "lucky_numbers":[7,13,22],
            },
            {
                "id": self._generateId(),
                "first_name":"Jane",
                "last_name": self.last_name,
                "age": 35,
                "lucky_numbers":[10,4,3],
            },
              {
                "id": self._generateId(),
                "first_name":"Jimmy",
                "last_name": self.last_name,
                "age": 5,
                "lucky_numbers":[1],
            }
        ]

    def _generateId(self):
        return randint(0, 99999999)
    
    def add_member(self, member):
        new_member = {
            "id": member.get("id",self._generateId()),
            "first_name": member.get("first_name"),
            "last_name": self.last_name,
            "age": member.get("age"),
            "lucky_numbers": member.get("lucky_numbers"),
        }
        self._members.append(new_member)
        return new_member

    def delete_member(self, id):
        for member in self._members:
            if member["id"] == id:
                self._members.remove(member)
                return {"done": True}
        return {"done": False}


    def get_member(self, id):
        for member in self._members:
            if member.get("id") == id:
                return member
        return None 

    def get_all_members(self):
        return self._members