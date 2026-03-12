from backend.orchestrator import Orchestrator
from backend.solver import Solver, GuessMethod
from backend.validator import Validator

from colorama import init

from backend.word import Hint, Word

# init(autoreset=True)   # Colorama
game = Orchestrator.get_instance(method=GuessMethod.RANDOM)
won: bool = False

# Display welcome message
print(game.start_game(total_turns=6, random_answer=True) + "\n")

while game.get_turn() <= game.get_total_turns():
    guess = game.solver.guess()
    won, hints = game.validator.validate_guess(guess)

    game.solver.add_prev_guess(Word(value=guess.get_value(), hints=hints))

    # Display turn info
    print(f"Intento {game.get_turn()}: {guess} {game.validator.to_console_view(hints)}\n")

    if won:
        break

    game.next_turn()

# Display game finished message
print(game.finish_game(won))

prev_guesses = game.solver.get_prev_guesses()

# Debug
print("\nPrev guesses: ")
for i in range(len(prev_guesses)):
    print(f"{i}: {prev_guesses[i]}")
