#!/usr/bin/env python3
from brain_games.logic import logic
from random import randint


game_rules = 'What is the result of the expression?'

operations = ['+', '-', '*']


def calculate(num1, num2, operator):
    match operator:
        case '+':
            return num1 + num2
        case '-':
            return num1 - num2
        case '*':
            return num1 * num2
        case _:
            return 'Неизвестный оператор'


def set_game():
    first_number = randint(1, 10)
    second_number = randint(1, 10)
    operator = operations[randint(0, 2)]
    question = f'{first_number} {operator} {second_number}'
    wright_answer = str(calculate(first_number, second_number, operator))
    return question, wright_answer


def calc_game():
    logic(game_rules, set_game)


def main():
    calc_game()


if __name__ == '__main__':
    main()
