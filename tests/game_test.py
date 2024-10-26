import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from my_game import MyGame
from game_exception import GameException

class GameTest(unittest.TestCase):
    
    def setUp(self):
        """Initilisiert die MyGame-Instanz vor jedem Test."""
        self.game = MyGame()
    
    def test_define_card_success_1(self):
        """Testet, ob eine Karte mit dem richtigen Namen erstellt wurde."""
        self.game.define_card("Sauron")
        self.assertIn("Sauron", self.game.cards)
        self.assertEqual(self.game.cards["Sauron"], {})

    def test_define_card_duplicate_1(self):
        """Testet, ob bereits eine Karte mit demselben Namen besteht und die Exception geworfen wird."""
        self.game.define_card("Sauron")
        with self.assertRaises(GameException) as context:
            self.game.define_card("Sauron")
        self.assertEqual(str(context.exception), "Error! Card Sauron is already defined.")
    
if __name__ == "__main__":
    unittest.main()