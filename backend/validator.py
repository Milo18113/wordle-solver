from backend.word import Word
from backend.word import Hint

import random
import os

class Validator:
    _answer: Word

    def choose_answer_from(self, filename: str, random_choice: bool) -> None:
        if not random_choice:
            self._answer = Word("adult")
            return

        # Construimos la ruta hacia la carpeta repositories
        file_path = os.path.join("repositories", filename)

        with open(file_path, "r", encoding="utf-8") as file:
            words = [line.strip() for line in file if line.strip()]

        if len(words) == 0:
            raise ValueError("El archivo no contiene palabras válidas.")

        self._answer = Word(random.choice(words))

    def validate_guess(self, guess_word: Word) -> tuple[bool, list[Hint]]:
        answer = self._answer
        guess = str(guess_word)

        if answer == guess:
            return True, [Hint.GREEN for i in range(5)]
        
        hints = []
        for i in range(5):
            if answer.get_value()[i] == guess[i]:
                hints.append(Hint.GREEN)
            elif guess[i] in answer.get_value():
                hints.append(Hint.YELLOW)
            else:
                hints.append(Hint.GREY)

        return False, hints

    def get_answer(self):
        return self._answer


    # for console only
    def to_console_view(self, hints: list[Hint]) -> str:
        view = "["
        for item in hints:
            view += item.__str__()
        return view + "]"