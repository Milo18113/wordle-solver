from enum import Enum
from colorama import Fore

class GuessMethod(Enum):
    RANDOM = "Random"
    BRUTE_FORCE = "Brute Force"
    WORD_PREDICTION = "Word Prediction"

class Hint(Enum):
    GREY = 0
    YELLOW = 1
    GREEN = 2

    def __str__(self) -> str:
        if self == Hint.GREY:
            return f"{Fore.WHITE}O{Fore.RESET}"
        if self == Hint.YELLOW:
            return f"{Fore.YELLOW}O{Fore.RESET}"
        return f"{Fore.GREEN}O{Fore.RESET}"