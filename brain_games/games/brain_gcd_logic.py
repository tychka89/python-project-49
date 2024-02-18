#!/usr/bin/env python3
from brain_games.logic import logic
from random import randint


game_rules = 'Find the greatest common divisor of given numbers.'


def gcd(num1, num2):
    if num2 == 0:
        return num1
    return gcd(num2, num1 % num2)


def set_game():
    first_number = randint(1, 100)
    second_number = randint(1, 100)
    question = f'{first_number} {second_number}'
    wright_answer = str(gcd(first_number, second_number))
    return question, wright_answer


def gcd_game():
    logic(game_rules, set_game)


def main():
    gcd_game()


if __name__ == '__main__':
    main()
