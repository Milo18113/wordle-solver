from .solver import GuessMethod, Solver
from .word import Word
from .config import word_dictionary

import os
import random

class RandomSolver(Solver):
    def __init__(self):
        super().__init__()
    
    def guess(self) -> Word:
        self.update_knowledge()

        # Obtener todas las palabras del diccionario
        file_path = os.path.join("repositories", word_dictionary)
        words = []

        with open(file_path, "r", encoding="utf-8") as file:
            words = [line.strip() for line in file if line.strip()]

        if len(words) == 0:
            raise ValueError("El archivo no contiene palabras válidas.")

        return Word(value=random.choice(words))