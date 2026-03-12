from .solver import Solver
from .word import Word

class WordPredictionSolver(Solver):
    def __init__(self):
        super().__init__()
        
    def guess(self) -> Word:
        self.update_knowledge()
        guess_str: str = ""
        # TODO: Implementar lógica para adivinar la palabra
        return Word(guess=guess_str)