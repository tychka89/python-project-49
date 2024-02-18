#!/usr/bin/env python3
from brain_games.logic import logic
from random import randint


game_rules = 'What number is missing in the progression?'


def generate_progression(start, step, length):
    progression = []
    for i in range(length):
        progression.append(start + step * i)
    return progression


def set_game():
    first_step = randint(1, 10)
    step = randint(1, 10)
    length = randint(5, 10)
    progression = generate_progression(first_step, step, length)
    random_index = randint(0, len(progression) - 1)
    hidden_index = progression[random_index]
    wright_answer = str(hidden_index)
    progression[random_index] = '..'
    question = ' '.join(map(str, progression))
    return question, wright_answer


def progression_game():
    logic(game_rules, set_game)


def main():
    progression_game()


if __name__ == '__main__':
    main()
