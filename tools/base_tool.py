from abc import ABC, abstractmethod
from models.action import Action


class BaseTool(ABC):

    @abstractmethod
    def execute(self, action: Action):
        pass