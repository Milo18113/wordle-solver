from .word import Word
from .solver import Solver
from .config import word_dictionary

import random
import os

class BruteForceSolver(Solver):
    def __init__(self):
        super().__init__()

    def guess(self) -> Word:
        self.update_knowledge()
        self.update_possible_guesses()
        return self.get_highest_score_word()

    def update_possible_guesses(self) -> None:
        """
        Adds words with higher or equal [score] to the closest previous guess. 
        Additional [score] is earned for having a known [yellow char] in another position.
        """
        # First try
        if len(self._prev_guesses) == 0:        
            self._possible_guesses = self._starter_words.copy()
            random.shuffle(self._possible_guesses)
            return
        
        # Obtener todas las palabras del diccionario
        file_path = os.path.join("repositories", word_dictionary)
        words = []

        with open(file_path, "r", encoding="utf-8") as file:
            words = [line.strip() for line in file if line.strip()]

        if len(words) == 0:
            raise ValueError("El archivo no contiene palabras válidas.")

        # Filter words
        self._possible_guesses = []
        closest = self._my_answer
        for item in words:
            if item in self._prev_guesses:
                continue
            eval = self.evaluate_word(Word(item))
            if eval.get_score() >= closest.get_score():
                self._possible_guesses.append(eval)