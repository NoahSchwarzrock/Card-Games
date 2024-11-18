import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from my_game import MyGame
from game_exception import GameException


class GameTest(unittest.TestCase):

    def setUp(self):
        """Initializes the MyGame instance before each test."""
        self.game = MyGame()

    def test_define_card_success_1(self):
        """Tests if a card is created with the correct name."""
        self.game.define_card("Sauron")
        self.assertIn("Sauron", self.game.cards)
        self.assertEqual(self.game.cards["Sauron"], {})

    def test_define_card_duplicate_1(self):
        """Tests if a card with the same name already exists and raises an exception."""
        self.game.define_card("Sauron")
        with self.assertRaises(GameException) as context:
            self.game.define_card("Sauron")
        self.assertEqual(
            str(context.exception), "Error! Card Sauron is already defined."
        )

    def test_define_card_property_success_1(self):
        """Tests if a property is created correctly."""
        self.game.define_property("power", "integer")
        self.assertIn("power", self.game.properties)
        self.assertEqual(self.game.properties["power"], "integer")

    def test_define_card_property_success_2(self):
        """Tests if a property is created correctly."""
        self.game.define_property("type", "string")
        self.assertIn("type", self.game.properties)
        self.assertEqual(self.game.properties["type"], "string")

    def test_define_card_property_duplicate_1(self):
        """Tests if a property with the same name already exists and raises an exception."""
        self.game.define_property("power", "integer")
        with self.assertRaises(GameException) as context:
            self.game.define_property("power", "integer")
        self.assertEqual(
            str(context.exception), "Error! Property power is already defined."
        )

    def test_define_card_property_duplicate_2(self):
        """Tests if a property with the same name already exists and raises an exception."""
        self.game.define_property("type", "string")
        with self.assertRaises(GameException) as context:
            self.game.define_property("type", "string")
        self.assertEqual(
            str(context.exception), "Error! Property type is already defined."
        )

    def test_define_card_property_wrong_type_1(self):
        """Tests if a property raises an exception when a property is defined with a wrong type."""
        with self.assertRaises(GameException) as context:
            self.game.define_property("type", "float")
        self.assertEqual(
            str(context.exception),
            "Error! Property must be of type integer or string not float.",
        )

    def test_set_card_property_success_1(self):
        """Tests if a property is correctly assigned to a card"""
        self.game.define_card("Sauron")
        self.assertIn("Sauron", self.game.cards)
        self.game.define_property("power", "integer")
        self.assertIn("power", self.game.properties)
        self.game.set_property("Sauron", "power", 10)
        self.assertEqual(self.game.cards["Sauron"], {"power": 10})

    def test_set_card_property_success_2(self):
        """Tests if a property is correctly assigned to a card"""
        self.game.define_card("Sauron")
        self.assertIn("Sauron", self.game.cards)
        self.game.define_property("power", "integer")
        self.assertIn("power", self.game.properties)
        self.game.define_property("type", "string")
        self.assertIn("type", self.game.properties)
        self.game.set_property("Sauron", "power", 10)
        self.game.set_property("Sauron", "type", "Eldrazzi")
        self.assertEqual(self.game.cards["Sauron"], {"power": 10, "type": "Eldrazzi"})

    def test_set_card_property_but_card_does_not_exist(self):
        """Tests if an exception is raised when the card does not exist."""
        self.game.define_property("power", "integer")
        self.assertIn("power", self.game.properties)
        with self.assertRaises(GameException) as context:
            self.game.set_property("Sauron", "power", 10)
        self.assertEqual(str(context.exception), "Error! Card Sauron does not exist.")

    def test_set_card_property_but_property_does_not_exist(self):
        """Tests if an exception is raised when the property does not exist."""
        self.game.define_card("Sauron")
        self.assertIn("Sauron", self.game.cards)
        with self.assertRaises(GameException) as context:
            self.game.set_property("Sauron", "type", "Eldrazzi")
        self.assertEqual(str(context.exception), "Error! Property type does not exist.")

    def test_set_card_property_but_value_does_not_match_property(self):
        """Tests if an exception is raised when the value type does not match the property type."""
        self.game.define_card("Sauron")
        self.assertIn("Sauron", self.game.cards)
        self.game.define_property("power", "integer")
        self.assertIn("power", self.game.properties)
        with self.assertRaises(GameException) as context:
            self.game.set_property("Sauron", "power", "Eldrazzi")
        self.assertEqual(
            str(context.exception),
            "Error! Type of Eldrazzi is string, but the type for power is integer.",
        )

    def test_set_integer_rule_success_1(self):
        self.game.define_property("power", "integer")
        self.assertIn("power", self.game.properties)
        self.game.set_rule("power", operation=">")
        self.assertIn("power", self.game.rules)
        self.assertEqual(self.game.rules["power"], ">")

    def test_set_string_rule_success_1(self):
        self.game.define_property("type", "string")
        self.assertIn("type", self.game.properties)
        self.game.set_rule("type", winning_name="Eldrazi", losing_name="Human")
        self.assertIn("type", self.game.rules)
        self.assertEqual(
            self.game.rules["type"], {"winning_name": "Eldrazi", "losing_name": "Human"}
        )

    def test_set_integer_rule_duplicate(self):
        self.game.define_property("power", "integer")
        self.assertIn("power", self.game.properties)
        self.game.set_rule("power", operation=">")
        self.assertIn("power", self.game.rules)
        with self.assertRaises(GameException) as context:
            self.game.set_rule("power", operation=">")
        self.assertEqual(
            str(context.exception),
            "Error! The rule with property name power is already defined.",
        )

    def test_set_string_rule_duplicate(self):
        self.game.define_property("type", "string")
        self.assertIn("type", self.game.properties)
        self.game.set_rule("type", winning_name="Eldrazi", losing_name="Human")
        self.assertIn("type", self.game.rules)
        with self.assertRaises(GameException) as context:
            self.game.set_rule("type", winning_name="Eldrazi", losing_name="Human")
        self.assertEqual(
            str(context.exception),
            "Error! The rule with property name type, winning name Eldrazi and losing name Human is already defined.",
        )

    def test_set_integer_rule_but_property_is_not_defined(self):
        with self.assertRaises(GameException) as context:
            self.game.set_rule("power", operation=">")
        self.assertEqual(
            str(context.exception), "Error! The property power is not defined."
        )

    def test_set_integer_rule_but_operation_does_not_fit(self):
        self.game.define_property("power", "integer")
        self.assertIn("power", self.game.properties)
        with self.assertRaises(GameException) as context:
            self.game.set_rule("power", operation="=")
        self.assertEqual(
            str(context.exception),
            "Error! The property power is an integer and requires a comparison operation (<, >).",
        )

    def test_set_string_rule_with_same_winning_and_loosing_name(self):
        self.game.define_property("type", "string")
        self.assertIn("type", self.game.properties)
        self.game.set_rule("type", winning_name="Eldrazzi", losing_name="Eldrazzi")
        self.assertIn("type", self.game.rules)
        with self.assertRaises(GameException) as context:
            self.game.set_rule("type", winning_name="Eldrazzi", losing_name="Eldrazzi")
        self.assertEqual(
            str(context.exception),
            "Error! The rule with property name type, winning name Eldrazzi and losing name Eldrazzi is already defined.",
        )

    def test_get_card_success_1(self):
        self.game.define_card("Sauron")
        self.assertIn("Sauron", self.game.cards)
        self.assertEqual(self.game.get("card", "Sauron"), ["Sauron"])

    def test_get_card_success_2(self):
        self.game.define_card("Sauron")
        self.assertIn("Sauron", self.game.cards)
        self.game.define_card("Emrakul")
        self.assertIn("Emrakul", self.game.cards)
        self.assertEqual(self.game.get("card", "*"), ["Sauron", "Emrakul"])

    def test_get_card_thats_not_defined_1(self):
        self.assertEqual(self.game.get("card", "Sauron"), [])

    def test_get_property_success_1(self):
        self.game.define_property("power", "integer")
        self.assertIn("power", self.game.properties)
        self.assertEqual(self.game.get("property", "power"), ["power:integer"])

    def test_get_property_success_2(self):
        self.game.define_property("power", "integer")
        self.assertIn("power", self.game.properties)
        self.game.define_property("type", "string")
        self.assertIn("type", self.game.properties)
        self.assertEqual(
            self.game.get("property", "*"), ["power:integer", "type:string"]
        )

    def test_get_property_thats_not_defined_1(self):
        self.assertEqual(self.game.get("property", "power"), [])

    def test_get_rule_success_1(self):
        self.game.define_property("power", "integer")
        self.assertIn("power", self.game.properties)
        self.game.set_rule(property_name="power", operation=">")
        self.assertIn("power", self.game.rules)
        self.assertEqual(self.game.get("rule", "power"), ["power>"])

    def test_get_rule_success_2(self):
        self.game.define_property("power", "integer")
        self.assertIn("power", self.game.properties)
        self.game.define_property("type", "string")
        self.assertIn("type", self.game.properties)
        self.game.set_rule(property_name="power", operation=">")
        self.assertIn("power", self.game.rules)
        self.game.set_rule(
            property_name="type", winning_name="Human", losing_name="Eldrazi"
        )
        self.assertIn("type", self.game.rules)
        self.assertEqual(self.game.get("rule", "*"), ["power>", "type:Human>Eldrazi"])

    def test_get_rule_thats_not_defined_1(self):
        self.assertEqual(self.game.get("rule", "power"), [])

    def test_search_for_wrong_type_in_get_function_1(self):
        with self.assertRaises(GameException) as context:
            self.game.get("person", "Sauron")
        self.assertEqual(
            str(context.exception),
            "Error! You can only search for card, type or rule in this method!",
        )

    def test_search_for_wrong_type_in_get_function_2(self):
        with self.assertRaises(GameException) as context:
            self.game.get("card", 3)
        self.assertEqual(str(context.exception), "Error! Name has to be a string!")


if __name__ == "__main__":
    unittest.main()
