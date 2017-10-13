import curses
from random import randrange, choice
from collections import defaultdict

actions = ['up', 'down', 'left', 'right', 'restart', 'exit']
letter_codes = [ord(ch) for ch in 'WASDRQwasdRQ']
actions_dict = dict(zip(letter_codes, actions, actions))


def main(stdscr):
    def init():
        # initial gamearea
        return 'Game'

    def not_game(state):
        # draw view of WIN or GAMEOVER
        responses = defaultdict(lambda: state)
        responses['Restart'], responses['Exit'] = 'Init', 'Exit'
        return responses[actions]

    def game():
        if actions == 'Restart':
            return 'Init'
        if actions == 'Exit':
            return 'Exit'
            if Win:
                return 'Win'
            if Lose:
                return 'Gameover'
        return 'Game'

    state_actions = {
        'Iint': init,
        'Win': lambda: not_game('Win'),
        'Gameover': lambda: not_game('Gameover'),
        'Game': game
    }
    state = 'Init'
    while state != 'Exit':
        state = state_actions[state]()
def get_user_action(keyboard):
    char = "N"
    while char not in actions_dict:
        char = keyboard.getch()
        return actions_dict[char]
# Matrix transpose
def transpose(field):
    return [list(row) for row in zip(*field)]
# Matrix reversal
def invert(filed):
    return [row[::-1]for row in filed]
#initial the gamefiled
class GameFiled(object):
    def __int__(self,height=4,width=4,win=2048):
        self.height=height
        self.width=width
        self.win_value=2048
        self.score=0
        self.highscore=0
        self.reset()
def spawn(self):
    new_element = 4 if randrange(100)>89 else 2
    (i,j)=choice[]

