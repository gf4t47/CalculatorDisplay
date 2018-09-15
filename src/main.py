import functools
import json
from typing import List, Tuple

import svgwrite

from src.layout.board import Board
from matplotlib import pyplot as pl
from matplotlib import collections as mc


def _draw(lines: List[Tuple[Tuple[int, int], Tuple[int, int]]]) -> None:
    lc = mc.LineCollection(lines)
    fig, ax = pl.subplots()
    ax.add_collection(lc)
    ax.autoscale()
    ax.margins(0.1)
    pl.gca().invert_yaxis()
    pl.show()


def _save_json(num: int, lines: List[Tuple[Tuple[int, int], Tuple[int, int]]]):
    file_name = f'../data/{num}.json'
    with open(file_name, 'w') as f:
        json.dump(lines, f)
    return file_name


def _load_json(file_name: str):
    with open(file_name, 'r') as f:
        return json.load(f)


def _svg(num: int, lines: List[Tuple[Tuple[int, int], Tuple[int, int]]], size: Tuple[int, int]) -> None:
    border = 10
    width, height = size
    dwg = svgwrite.Drawing(f'../data/{num}.svg', (width + border * 2, height + border * 2), profile='full')
    for (start_x, start_y), (end_x, end_y) in lines:
        dwg.add(dwg.line((start_x + border, start_y + border), (end_x + border, end_y + border), stroke=svgwrite.rgb(10, 10, 16, '%')))
    dwg.save()


def display(num: int) -> None:
    size = 600, 200
    board = Board(size, True)
    digits = board.digitalize(num)
    lines = functools.reduce(lambda accu, cur: accu + cur, [digit.lines for digit in digits], [])

    file_name = _save_json(num, lines)
    json_obj = _load_json(file_name)
    _svg(num, json_obj, size)

    _draw(json_obj)


display(70128)
