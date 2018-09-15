import functools
from typing import List, Tuple

from src.layout.board import Board
import pylab as pl
from matplotlib import collections as mc


def _draw(lines: List[Tuple[Tuple[int, int], Tuple[int, int]]]) -> None:
    lc = mc.LineCollection(lines)
    fig, ax = pl.subplots()
    ax.add_collection(lc)
    ax.autoscale()
    ax.margins(0.1)
    pl.show()


def display(num: int) -> None:
    board = Board(600, 200)
    digits = board.digitalize(num)
    lines = functools.reduce(lambda accu, cur: accu + cur, [digit.lines for digit in digits], [])
    _draw(lines)


display(70128)
