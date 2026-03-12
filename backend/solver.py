from .word import Hint, Word
from .config import word_dictionary

import os
import random

class Solver: 
    # _skill_level: int
    _prev_guesses: list[Word]
    _possible_guesses: list[Word]          # o tree

    _yellow_chars: set
    _grey_chars: set

    _starter_words: list[Word]
    _my_answer: Word

    # def __init__(self, skill_level: int = 1):
    def __init__(self):
        # if skill_level < 1 or skill_level > 5:
        #     raise ValueError("Skill level must be between 1 and 5")
        # self._skill_level = skill_level

        self._prev_guesses = []
        self._possible_guesses = []     # o tree

        self._yellow_chars = set()
        self._grey_chars = set()

        self._starter_words = [
            Word("brown", score=10),
            Word("tales", score=10),
            Word("trial", score=10),
        ]
        self._my_answer = Word("_____")

    def get_prev_guesses(self):
        return self._prev_guesses
    
    def get_possible_guesses(self):
        return self._possible_guesses
    
    def add_prev_guess(self, guess: Word):
        self._prev_guesses.append(guess)

    def add_yellow_char(self, char: str):
        if len(char) != 1:
            raise ValueError("Character added to solver._yellow_chars must be of length 1")
        self._yellow_chars.add(char)

    def get_yellow_chars(self):
        return self._yellow_chars
    
    def add_grey_char(self, char: str):
        if len(char) != 1:
            raise ValueError("Character added to solver._grey_chars must be of length 1")
        self._grey_chars.add(char)

    def get_grey_chars(self):
        return self._grey_chars
    
    


    def guess(self) -> Word:
        self.update_knowledge()
        # self.update_possible_guesses_bf(word_dictionary)        
        # guess: Word # choose word with highest score from possible_guesses
        ## Test
        guess_str = self.get_random_guess(word_dictionary)
        #
        return Word(value=guess_str)
    
    def get_random_guess(self, filename: str) -> str:
        # Construimos la ruta hacia la carpeta repositories
        file_path = os.path.join("repositories", filename)

        with open(file_path, "r", encoding="utf-8") as file:
            words = [line.strip() for line in file if line.strip()]

        if len(words) == 0:
            raise ValueError("El archivo no contiene palabras válidas.")

        return random.choice(words)
    
    def update_knowledge(self):
        if len(self._prev_guesses) == 0:        # First try
            return
        
        latest = self._prev_guesses[-1]
        next_my_answer = self._my_answer.get_value()
        next_my_hints = self._my_answer.get_hints()

        for i in range(5):
            char, hint = latest.get_char_hint(i)
            if (hint == Hint.GREEN):
                # next_my_answer[i] = char
                # next_my_hints[i] = hint
                pass
            if (hint == Hint.YELLOW):
                self.add_yellow_char(char)
            if (hint == Hint.GREY):
                self.add_grey_char(char)
    
    # Using score based on position and char matching (Brute Force)
    def update_possible_guesses_bf(self, filename: str):
        if len(self._prev_guesses) == 0:        # First try
            self._possible_guesses = self._starter_words
            return
        
        my_answer = ""
        for i in range(5):
            closest = self.choose_closest_prev_guess()        # Temporary
            char, hint = closest.get_char_hint(i)
            # if 
        pass

    def choose_closest_prev_guess(self) -> Word:
        # return self._prev_guesses[-1]
    
        # prev guesses cannot be empty if this method is accessed
        max = self._prev_guesses[0]
        for item in self._prev_guesses:
            if item.get_greens() == max.get_greens():
                continue
            if item.get_greens() > max.get_greens():
                max = item

        return max

    
        