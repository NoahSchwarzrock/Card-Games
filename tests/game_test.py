import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

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
        self.assertEqual(str(context.exception), "Error! Card Sauron is already defined.")
        
    def test_define_card_property_success_1(self):
        """Tests if a property is created correctly."""
        self.game.define_property("power", int)
        self.assertIn("power", self.game.properties)
        self.assertEqual(self.game.properties["power"], {"type": int})
        
    def test_define_card_property_duplicate_1(self):
        """Tests if a property with the same name already exists and raises an exception."""
        self.game.define_property("power", int)
        with self.assertRaises(GameException) as context:
            self.game.define_property("power", int)
        self.assertEqual(str(context.exception), "Error! property power is already defined.")
        
        
        
if __name__ == "__main__":
    unittest.main()