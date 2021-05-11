from main.domain.helper.Exception import UnauthorisedAction


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
        raise UnauthorisedAction("Not permitted to change oid.")

    def __eq__(self, other) -> bool:
        if type(other) is QLObject:
            return self.oid == other.oid