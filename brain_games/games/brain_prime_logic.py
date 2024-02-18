#!/usr/bin/env python3
from brain_games.logic import logic
from random import randint


game_rules = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def set_game():
    question = randint(1, 100)
    wright_answer = 'yes' if prime(question) else 'no'
    return question, wright_answer


def prime_game():
    logic(game_rules, set_game)


def main():
    prime_game()


if __name__ == '__main__':
    main()
