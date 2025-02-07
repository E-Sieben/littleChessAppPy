import js2py
from ConvertedBot import *


def move(board):
    js2py.translate_file("JsBogoBot", "ConvertedBot.py")
    ConvertedBot.move(board)
