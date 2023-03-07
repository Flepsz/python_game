# ---------------------------------------------------------------------------
# Created By  : Luis Felipe Pereira
# Created Date: 02/26/2023
# Version 1.0
# ---------------------------------------------------------------------------

from threading import Timer
from random import randint
import os

attempts = 3
damage = 0
life = 50
num_inputted = 0
match = 0

color = {
    'red': '\33[7;91m',
    'yellow': '\33[7;93m',
    'blue': '\33[7;36m',
    'green': '\33[7;92m',
    'cyan': '\33[7;96m',
    'r': '\33[1;31m',
    'c': '\33[m'
}


def rules():
    """
    Shows the rules of the game.
    :return:
    """
    print('')
    print('  ' * 16, ' <<<<< MATCH YOUR LUCKY NUMBER >>>>> ')
    print('')
    print('==' * 23, ' RULES ', '==' * 24)
    print('A RANDOM NUMBER WILL BE DRAWN AND YOU WILL TRY TO MATCH THE NUMBER')
    print('YOU WILL HAVE {}50 LIFE{}, {}3 TRIES{} AND {}20 SECONDS{}'.format(color['red'], color['c'], color['yellow'],
                                                                             color['c'], color['blue'], color['c']))
    print('EACH FAILED ATTEMPT, YOUR LIFE WILL BE DISCOUNTED ACCORDING TO THE DIFFERENCE '
          'BETWEEN YOUR NUMBER AND THE DRAWN NUMBER')
    print('===' * 35)


def start_game():
    """
    Menu to user input, and start the game.
    :return:
    """
    op = int(input('[1] START: '))
    while op != 1:
        print('OPTION INVALID, TRY AGAIN!')
        print('')
        op = int(input('[1] START: '))
    if op == 1:
        print('')
        print('LET THE GAME BEGIN!')
        print('')
        print('-=' * 17)
        t = Timer(15.0, time_stop)
        t.start()


def logic():
    """
    Principal logic of game.
    :return:
    """
    global num_inputted, attempts, life, match
    while attempts > 0 and num_inputted != lucky_number and life > 0:
        attempts -= 1
        lives_print()
        num_inputted = int(input('Type your number: \n'))
        print('-=' * 17)
        life -= taken_damage()
        if lucky_number == num_inputted:
            match += 1
            win_message()


def random_num():
    """
    Generate the number that the user will try to match.
    :return:
    """
    num = randint(1, 100)
    return num


def taken_damage():
    """
    Amount of damage that the user will take.
    :return:
    """
    global damage
    damage = abs(lucky_number - num_inputted)
    return damage


def lives_print():
    """
    Print user remain lives.
    :return:
    """
    print('Lives: {}{}{}'.format(color['r'], life, color['c']))


def number_reveal():
    """
    Reveals the secret number
    :return:
    """
    print('The lucky number was = {}{}{}'.format(color['green'], lucky_number, color['c']))


def lose_message():
    """
    Message when user lose the game.
    :return:
    """
    if match == 0:
        print('{}YOU LOSE, TRY AGAIN!{}\n'.format(color['red'], color['c']))
        time_stop("GAME OVER!!")
        number_reveal()


def win_message():
    """
    Message when user win the game.
    :return:
    """
    print("{}YOU'RE GOD DAMN RIGHT.{}\n".format(color['cyan'], color['c']))
    time_stop("GAME OVER!!")


def time_stop(msg="THE TIME IS UP, GAME OVER!"):
    """
    Logic to close the game when time ends.
    :param msg:
    :return:
    """
    print(msg)
    pid = os.getpid()
    os.kill(pid, 0)


lucky_number = random_num()
rules()
start_game()
logic()
lose_message()
time_stop()
