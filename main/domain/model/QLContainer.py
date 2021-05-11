from main.domain.helper.Exception import UnauthorisedAction
from main.domain.model.QLObject import QLObject


class QLContainer:
    """
    Qilin Container\n
    A class represent a container.\n
    A QLContainer could contain QLObject or another QLContainer.
    """
    __oid: int
    container: list

    def __init__(self, oid: int):
        self.__oid = oid
        self.container = []

    @property
    def oid(self):
        return self.__oid

    @oid.setter
    def oid(self, other):
        raise UnauthorisedAction("Not permitted to change oid.")

    def add(self, other):
        if type(other) is QLContainer or QLObject:
            self.container.append(other)
        else:
            raise UnauthorisedAction()

    def delete(self, other):
        if type(other) is int:
            self.container.pop(other)
        elif type(other) is QLObject or QLContainer:
            self.container.pop(self.container.index(other))
        else:
            raise UnauthorisedAction()

    def __eq__(self, other) -> bool:
        if type(other) is QLContainer:
            return self.oid == other.oid
