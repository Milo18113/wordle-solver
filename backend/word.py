from enum import Enum

from colorama import Fore

class Hint(Enum):
    GREY = 0
    YELLOW = 1
    GREEN = 2

    def __str__(self) -> str:
        if self == Hint.GREY:
            return f"{Fore.WHITE}O{Fore.RESET}"
        if self == Hint.YELLOW:
            return f"{Fore.YELLOW}O{Fore.RESET}"
        # if self == Hint.GREEN:
        return f"{Fore.GREEN}O{Fore.RESET}"


class Word:
    _value: str
    _score: int     # possibility
    _hints: list[Hint] | None

    def __init__(self, value: str, score: int = 0, hints: list | None = None):
        self.set_value(value)
        self.set_score(score)
        self.set_hints(hints)

    def set_value(self, value: str):
        if (len(value) != 5):
            raise ValueError("Word must be 5 letters long")
        self._value = value.lower()

    def get_value(self):
        return self._value
    
    def set_score(self, score: int):
        if (score < 0):
            raise ValueError("Score must be non-negative")
        self._score = score
    
    def get_score(self):
        return self._score

    def add_score(self, score: int):
        if (self._score + score < 0):
            raise ValueError("Change of score must be non-negative")
        self._score += score

    def set_hints(self, hints: list | None):
        if hints is None:
            self._hints = None
        elif len(hints) != 5:
            raise ValueError("Hints must be None or a list with 5 positions")
        self._hints = hints

    def get_hints(self):
        return self._hints
    
    def has_hints(self):
        return self._hints is not None

    def get_char_hint(self, index: int) -> tuple[str, Hint]:
        if self._hints is None:
            raise ValueError(f"Word {self} has no hints")
        return self._value[index], self._hints[index]
    
    ## add getcharhint method
    
    # Based only on Green chars
    def get_greens(self) -> int:
        greens = 0
        for i in range(5):
            if self.get_char_hint(i)[1] == Hint.GREEN:
                greens += 1
        
        return greens

    def __str__(self):
        return f"{self._value} ({self._score})"
        # return f"{self._value} ({self._score}) [{self._hints}]"
        # return self._value
    
    def __eq__(self, other):
        if isinstance(other, Word):
            return self._value == other.get_value()
        if isinstance(other, str):
            return self._value == other
        return False
    
    ## comparator ?

