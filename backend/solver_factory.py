from .solver import GuessMethod
from .random_solver import RandomSolver
from .brute_force_solver import BruteForceSolver
from .word_prediction_solver import WordPredictionSolver

class SolverFactory:
    @staticmethod
    def create_solver(method: GuessMethod):
        if method == GuessMethod.RANDOM:
            return RandomSolver()
        elif method == GuessMethod.BRUTE_FORCE:
            return BruteForceSolver()
        elif method == GuessMethod.WORD_PREDICTION:
            return WordPredictionSolver()
        else:
            raise ValueError(f"Unknown solver method: {method}")