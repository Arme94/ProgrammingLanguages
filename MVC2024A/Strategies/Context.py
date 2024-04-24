
class ChangeState:
    def __init__(self, strategy):
        self.strategy = strategy

    def change_state(self):
        self.strategy.handle()