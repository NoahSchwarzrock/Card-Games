from typing import final

from game_exception import GameException
from my_game import MyGame
from game import Game

@final
class Factory:
    @staticmethod
    def create_game(name: str) -> Game:
        # raise GameException('')
        return MyGame(name)
    
    @staticmethod
    def load_game(path: str) -> Game:
        # raise GameException('')
        return MyGame.load_game(path)