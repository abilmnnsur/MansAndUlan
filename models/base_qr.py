from abc import ABC, abstractmethod


class BaseQR(ABC):

    def __init__(self, data: str):
        self.data = data

    @abstractmethod
    def get_formatted_data(self) -> str:
        pass

    @abstractmethod
    def get_type(self) -> str:
        pass
