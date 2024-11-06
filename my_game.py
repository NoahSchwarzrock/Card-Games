from Game import Game
from game_exception import GameException
from typing import Union, Optional


class MyGame(Game):
    def __init__(self):
        self.cards = {}
        self.properties = {}
        self.rules = {}

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
        if type not in ["integer", "string"]:
            raise GameException(
                f"Property must be of type integer or string not {type}."
            )
        self.properties[name] = type

    def set_property(
        self, card_name: str, property_name: str, value: Union[str, int]
    ) -> None:
        if card_name not in self.cards:
            raise GameException(f"Card {card_name} does not exist.")
        if property_name not in self.properties:
            raise GameException(f"Property {property_name} does not exist.")

        expected_type = self.properties[property_name]

        actual_type = (
            "integer"
            if isinstance(value, int)
            else "string" if isinstance(value, str) else type(value).__dict__
        )

        if expected_type != actual_type:
            raise GameException(
                f"Type of {value} is {actual_type}, but the type for {property_name} is {expected_type}."
            )
        self.cards[card_name][property_name] = value

    def set_rule(
        self,
        property_name: str,
        operation: Optional[str] = None,
        winning_name: Optional[str] = None,
        losing_name: Optional[str] = None,
    ) -> None:
        if property_name not in self.properties:
            raise GameException(f"The property {property_name} is not defined.")
        if property_name in self.rules and self.properties[property_name] == "integer":
            raise GameException(
                f"The rule with property name {property_name} is already defined."
            )
        if self.properties[property_name] == "integer" and operation not in ["<", ">"]:
            raise GameException(
                f"The property {property_name} is an integer and requires a comparison operation (<, >)."
            )
        if (
            property_name in self.rules
            and self.properties[property_name] == "string"
            and self.rules[property_name]["winning_name"] == winning_name
            and self.rules[property_name]["losing_name"] == losing_name
        ):
            raise GameException(
                f"The rule with property name {property_name}, winning name {winning_name} and losing name {losing_name} is already defined."
            )
        if operation is not None and winning_name is None and losing_name is None:
            self.rules[property_name] = operation
        elif operation is None and winning_name is not None and losing_name is not None:
            self.rules[property_name] = {
                "winning_name": winning_name,
                "losing_name": losing_name,
            }
        else:
            raise GameException(
                f"Invalid parameters for set_rule. Expected either (property_name, operation) or (property_name, winning_name, losing_name)."
            )

    def get(self, type: str, name: str) -> list[str]:
        if type not in ["card", "property", "rule"]:
            raise GameException("You can only search for card, type or rule in this method!")
        if type == "card":
            pass

    def save_to_file(self, path: str) -> None:
        pass

    def create_deck(self):  # -> Game:
        pass
