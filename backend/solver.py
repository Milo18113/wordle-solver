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

    # _yellow_chars: set
    _grey_chars: set

    _starter_words: list[Word]
    _my_answer: Word        # Always the closest guess

    def __init__(self):
        self._prev_guesses = []
        self._possible_guesses = []     # o tree

        # self._yellow_chars = set()
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

    # def add_yellow_char(self, char: str):
    #     if len(char) != 1:
    #         raise ValueError("Character added to solver._yellow_chars must be of length 1")
    #     self._yellow_chars.add(char)

    # def get_yellow_chars(self):
    #     return self._yellow_chars
    
    def add_grey_char(self, char: str):
        if len(char) != 1:
            raise ValueError("Character added to solver._grey_chars must be of length 1")
        self._grey_chars.add(char)

    def get_grey_chars(self):
        return self._grey_chars

    def isYellow(self, char: str) -> bool:
        for i in range(5):
            my_char, my_hint = self._my_answer.get_char_hint(i)
            if my_char == char and my_hint == Hint.YELLOW:
                return True
        return False
    
    
    ## Guess Logic ##

    @abstractmethod
    def guess(self) -> Word:
        raise NotImplementedError
    
    def update_knowledge(self) -> None:
        """Updates [my_answer] and [grey_chars] based on all the hints from all the prev guesses."""
        # First try
        if len(self._prev_guesses) == 0:        
            return
        
        latest = self._prev_guesses[-1]
        next_my_answer = list(self._my_answer.get_value())
        next_my_hints = list(self._my_answer.get_hints() or [Hint.GREY] * 5)  # but still wont be none

        for i in range(5):
            char, hint = latest.get_char_hint(i)
            if (hint == Hint.GREEN or hint == Hint.YELLOW):
                next_my_answer[i] = char
                next_my_hints[i] = hint
            if (hint == Hint.GREY):
                self.add_grey_char(char)
        
        self._my_answer = Word("".join(next_my_answer), hints=next_my_hints)

    def get_closest_prev_guess(self) -> Word:
        """Returns the previous guess with the most greens."""
        if len(self._prev_guesses) == 0:
            raise ValueError("No previous guesses available")

        max = self._prev_guesses[0]
        for item in self._prev_guesses:
            if item.get_greens() == max.get_greens():
                continue
            if item.get_greens() > max.get_greens():
                max = item

        return max

    def evaluate_word(self, word: Word) -> Word:
        """Returns a word with hints based on current knowledge and a score."""
        word_str = word.get_value()
        hints = []
        score: int = 0
        
        for i in range(5):
            my_char, my_hint = self._my_answer.get_char_hint(i)
            char = word_str[i]
            
            if char == my_char and my_hint == Hint.GREEN:
                hints.append(Hint.GREEN)
                score += 100
            elif self.isYellow(char) and my_char == char:
                hints.append(Hint.YELLOW)
                score += 10
            elif self.isYellow(char) and my_char != char:
                hints.append(Hint.YELLOW)
                score += 1
            else:
                hints.append(Hint.GREY)
        
        return Word(word_str, hints=hints, score=score)

    def get_highest_score_word(self) -> Word:
        """Gets it from [possible_guesses]"""
        highest_word = self._possible_guesses[0]

        for item in self._possible_guesses:
            if (item.get_score() > highest_word.get_score()):
                highest_word = item

        return highest_word
        