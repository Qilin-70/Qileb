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
        raise UnauthorisedAction()

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


class QLObject:
    """
    Qilin Object
    """
    __oid: int

    def __init__(self, oid: int):
        self.__oid = oid

    @property
    def oid(self):
        return self.__oid

    @oid.setter
    def oid(self, other):
        raise UnauthorisedAction()

    def __eq__(self, other) -> bool:
        if type(other) is QLObject:
            return self.oid == other.oid


class List:
    array: list

    def __init__(self):
        self.array = []

    def add(self):
        pass

    def get_by_index(self):
        pass

    def get_by_oid(self):
        pass

    def get_by_itself(self):
        pass

    def delete_by_index(self):
        pass

    def delete_by_oid(self):
        pass

    def delete_by_itself(self):
        pass


class UnauthorisedAction(Exception):
    def __init__(self, message="Action not permitted."):
        self.message = message
        super().__init__(message)
