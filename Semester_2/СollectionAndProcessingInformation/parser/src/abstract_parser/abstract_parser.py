from abc import ABC, abstractmethod


class AbstractParser(ABC):

    @staticmethod
    @abstractmethod
    def extract_all_text(path, ):
        pass
