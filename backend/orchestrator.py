from backend.solver import Solver
from backend.validator import Validator
from backend.config import word_dictionary

class Orchestrator:
    _turn: int
    _total_turns: int
    # app: StreamlitApp

    solver: Solver
    validator: Validator

    def __init__(self, solver: Solver, validator: Validator):
        self.solver = solver
        self.validator = validator

    def run(self, total_turns: int):
        # self.start_game(total_turns)
        # done: bool

        # while self.get_turn() <= self.get_total_turns():
        #     guess = self.solver.guess()
        #     done = self.validator.validate_guess(guess)
        #     if done:
        #         break
        #     self.solver.add_prev_guess(guess)
        #     self.next_turn()

        # return self.finish_game(done)
        pass

    def start_game(self, total_turns: int, random_answer: bool = True) -> str:
        self.validator.choose_answer_from(word_dictionary, random_answer)
        self._turn = 1
        self._total_turns = total_turns

        return "Game started! You have " + str(total_turns) + " turns to guess the word."

    def get_turn(self):
        return self._turn
    
    def get_total_turns(self):
        return self._total_turns
    
    def next_turn(self):
        # if self._turn +1 > self._total_turns:
        #     raise ValueError("No more turns left")
        self._turn += 1

    def finish_game(self, won: bool) -> str:
        if won:
            return "Congratulations! You guessed the word in " + str(self._turn) + " turns!"
        else:
            return f"Game over! The correct word was {self.validator.get_answer()}. Better luck next time!"

