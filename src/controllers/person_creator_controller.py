from src.models.sqlite.interfaces.people_repository import PeopleReposirotyInterface

class PersonCreatorController:
    def __init__(self, people_repository: PeopleReposirotyInterface) -> None:
        self.__people_repository = people_repository
        