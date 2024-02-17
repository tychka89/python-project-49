#!/usr/bin/env python3
import prompt


game_rounds = 3


def logic(game_rules, set_game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game_rules)
    for i in range(game_rounds):
        [question, wright_answer] = set_game()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')
        if user_answer != wright_answer:
            print(f'{user_answer} is wrong answer ;(. Correct answer was {wright_answer}.')
            print(f'Let\'s try again, {name}!')
            return
        print('Correct!')
    print(f'Congratulations, {name}!')
