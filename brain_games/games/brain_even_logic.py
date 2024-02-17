#!/usr/bin/env python3
from brain_games.logic import logic
from random import randint


game_rules = 'Answer "yes" if the number is even, otherwise answer "no".'


def set_game():
    question = randint(1, 100)
    wright_answer = 'yes' if question % 2 == 0 else 'no'
    return question, wright_answer


def even_game():
    logic(game_rules, set_game)


def main():
    even_game()


if __name__ == '__main__':
    main()
