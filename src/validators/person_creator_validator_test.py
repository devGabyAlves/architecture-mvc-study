from .person_creator_validator import person_creator_validator

class MockRequest:
    def __init__(self, body) -> None:
       self.body = body

def test_person_creator_validator():
    request = MockRequest({
        "first_name": "Gaby",
        "last_name": "Silva",
        "age": 21,
        "pet_id": 6
    })

    person_creator_validator(request)