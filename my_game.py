from Game import Game
from game_exception import GameException

class MyGame(Game):
    def __init__(self):
        self.cards = {}
        self.properties = {}
    
    def define_card(self, name: str) -> None:
        if name in self.cards:
            raise GameException(f"Card {name} is already defined.")
        else:
            self.cards[name] = {}
        
    def define_property(self, name: str, type: str) -> None:
        name = str(name).lower()
        type = str(type).lower()
        if name in self.properties:
            raise GameException(f"Property {name} is already defined.")
        elif type not in ["integer", "string"]:
            raise GameException(f"Property must be of type integer or string not {type}.")
        self.properties[name] = type
    
    def set_property(self, card_name: str, property_name: str, value: int) -> None:
        pass
    
    def set_rule(self, property_name: str, operation: str) -> None:
        pass
    
    def get(self, type: str, name: str) -> list[str]:
        pass
    
    def save_to_file(self, path: str) -> None:
        pass
    
    def create_deck(self): # -> Game:
        pass