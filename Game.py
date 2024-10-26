from abc import ABCMeta, abstractmethod
from typing import overload
from game_exception import GameException

class Game(metaclass=ABCMeta):
    @abstractmethod
    def define_card(self, name: str) -> None:
        # raise GameException('')
        pass
    
    @abstractmethod
    def define_property(self, name: str, type: str) -> None:
        # raise GameException('')
        pass
    
    @abstractmethod
    @overload
    def set_property(self, card_name: str, property_name: str, value: int) -> None:
        # raise GameException('')
        pass
    
    @abstractmethod
    def set_property(self, card_name: str, property_name: str, value: int) -> None:
        # raise GameException('')
        pass
    
    @abstractmethod
    @overload
    def set_rule(self, property_name: str, operation: str) -> None:
        # raise GameException('')
        pass
    
    @abstractmethod
    @overload
    def set_rule(self, property_name: str, winning_name: str, losing_name: str) -> None:
        # raise GameException('')
        pass
    
    @abstractmethod
    def get(self, type: str, name: str) -> list[str]:
        # raise GameException('')
        pass
    
    @abstractmethod
    def save_to_file(self, path: str) -> None:
        # raise GameException('')
        pass
    
    @abstractmethod
    def create_deck(self): # -> Game:
        pass