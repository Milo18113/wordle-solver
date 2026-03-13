from backend.orchestrator import Orchestrator
from backend.solver import GuessMethod
from backend.validator import Validator

from backend.word import Word

game = Orchestrator.get_instance(method=GuessMethod.BRUTE_FORCE)
won: bool = False

# Display welcome message
print(game.start_game(total_turns=6, random_answer=True) + "\n")

while game.get_turn() <= game.get_total_turns():
    guess = game.solver.guess()
    won, hints = game.validator.validate_guess(guess)

    game.solver.add_prev_guess(Word(value=guess.get_value(), hints=hints))

    # Display turn info
    print(f"Intento {game.get_turn()}: {guess} {game.validator.to_console_view(hints)}")
    my_ans = game.solver._my_answer
    print(f"My answer: {my_ans} {game.validator.to_console_view(my_ans.get_hints()) if my_ans.get_hints() is not None else ''}\n")

    if won:
        break

    game.next_turn()

# Display game finished message
print(game.finish_game(won))

prev_guesses = game.solver.get_prev_guesses()

# Debug
# print("\nPrev guesses: ")
# for i in range(len(prev_guesses)):
#     print(f"{i}: {prev_guesses[i]}")

# print("\nPossible guesses: ")
# for i in range(len(game.solver._possible_guesses)):
#     print(f"{i}: {game.solver._possible_guesses[i]}")

# print(game.finish_game(won))
