import curses
from random import randrange,choice
from collections import defaultdict

actions =['up','down','left','right','restart','exit']
letter_codes =[ord(ch) for ch in 'WASDRQwasdRQ']
actions(dict) =dict(zip(letter_codes,actions,actions))
def main(stdscr):
    def init():
        #initial gamearea
        return 'Game'
    def not_game(state):
        #draw view of WIN or GAMEOVER
        responses = defaultdict(lambda:state)
        responses['R']