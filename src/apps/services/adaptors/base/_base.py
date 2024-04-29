import abc


class Connection(abc.ABC):
    pass


class RemoveStorage(abc.ABC):

    @abc.abstractmethod
    def serviceMetadata() -> dict:
        """Переместить объект"""
        raise NotImplementedError

    @abc.abstractmethod
    def uploadFile() -> list:
        """Скорость объекта"""
        raise NotImplementedError

    @abc.abstractmethod
    def downloadFile() -> list:
        """Скорость объекта"""
        raise NotImplementedError
