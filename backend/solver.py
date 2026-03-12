from .word import Hint, Word
from .config import word_dictionary
from enum import Enum
from abc import ABC, abstractmethod

class GuessMethod(Enum):
    RANDOM = 1
    BRUTE_FORCE = 2
    WORD_PREDICTION = 3

class Solver(ABC): 
    _prev_guesses: list[Word]
    _possible_guesses: list[Word]          # o tree

    _yellow_chars: set
    _grey_chars: set

    _starter_words: list[Word]
    _my_answer: Word

    def __init__(self):
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
    
    
    ## Guess Logic ##

    @abstractmethod
    def guess(self) -> Word:
        raise NotImplementedError
    
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

    def get_closest_prev_guess(self) -> Word:
        # return self._prev_guesses[-1]
    
        # prev guesses cannot be empty if this method is accessed
        max = self._prev_guesses[0]
        for item in self._prev_guesses:
            if item.get_greens() == max.get_greens():
                continue
            if item.get_greens() > max.get_greens():
                max = item

        return max

    
        