class Game:
    def __init__(self):
        self.game_state_manager = GameStateManager("Player vs Computer")

    def run(self):
        while True:
            pass


class GameStateManager:
    def __init__(self, current_state: str):
        self.current_state = current_state

    def get_state(self):
        return self.current_state
    
    def set_state(self, state):
        self.current_state = state


if __name__ == '__main__':
    game = Game()
    game.run()
