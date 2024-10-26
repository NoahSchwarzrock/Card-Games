class GameException(Exception):
    def __init__(self, message: str):
        super(GameException, self).__init__(f"Error! {message}")