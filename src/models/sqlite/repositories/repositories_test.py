import pytest
from src.models.sqlite.settings import db_connection_handler
from .pets_repository import PetsRepository

db_connection_handler.connect_to_db()

@pytest.mark.skip(reason="Interaction with the bank")
def test_list_pets():
    repo = PetsRepository(db_connection_handler)
    response = repo.list_pets()
    print(response)

def test_delete_pet():
    name = "belinha"
    repo = PetsRepository(db_connection_handler)
    repo.delete_pets(name)