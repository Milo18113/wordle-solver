from .word import Word
from .solver import Solver

class BruteForceSolver(Solver):
    def __init__(self):
        super().__init__()

    def guess(self) -> Word:
        self.update_knowledge()
        guess_str: str = ""
        # TODO: Implementar lógica para adivinar la palabra
        return Word(guess=guess_str)

    # Using score based on position and char matching (Brute Force)
    def update_possible_guesses(self) -> None:
        if len(self._prev_guesses) == 0:        # First try
            self._possible_guesses = self._starter_words
            return
        
        my_answer: str = ""
        closest = self.get_closest_prev_guess()        # Temporary
        for i in range(5):
            char, hint = closest.get_char_hint(i)
            # if 
        pass

    