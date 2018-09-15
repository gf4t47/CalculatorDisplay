import functools
import json
from typing import List, Tuple

import svgwrite

from src.layout.board import Board
from matplotlib import pyplot as pl
from matplotlib import collections as mc

board_size = 600, 200


def _draw(lines: List[Tuple[Tuple[int, int], Tuple[int, int]]]) -> None:
    lc = mc.LineCollection(lines)
    fig, ax = pl.subplots()
    ax.add_collection(lc)
    ax.autoscale()
    ax.margins(0.1)
    pl.gca().invert_yaxis()
    pl.show()


def _save_json(num: int, lines: List[Tuple[Tuple[int, int], Tuple[int, int]]]) -> str:
    file_name = f'../data/{num}.json'
    with open(file_name, 'w') as f:
        json.dump(lines, f)
    return file_name


def _load_json(file_name: str) -> [List[List[int]]]:
    with open(file_name, 'r') as f:
        return json.load(f)


def _svg(num: int, lines: List[Tuple[Tuple[int, int], Tuple[int, int]]], size: Tuple[int, int]) -> str:
    border = 10
    width, height = size
    file_name = f'../data/{num}.svg'
    dwg = svgwrite.Drawing(file_name, (width + border * 2, height + border * 2), profile='tiny')
    for (start_x, start_y), (end_x, end_y) in lines:
        dwg.add(dwg.line((start_x + border, start_y + border), (end_x + border, end_y + border), stroke=svgwrite.rgb(10, 10, 16, '%')))
    dwg.save()
    return file_name


def _build_model(num: int, y_direct_down=True) -> List[Tuple[Tuple[int, int], Tuple[int, int]]]:
    board = Board(board_size, y_direct_down)
    digits = board.digitalize(num)
    return functools.reduce(lambda accu, cur: accu + cur, [digit.lines for digit in digits], [])


def write(num: int) -> str:
    file_name = _save_json(num, _build_model(num))
    json_obj = _load_json(file_name)
    return _svg(num, json_obj, board_size)


def display(num: int) -> None:
    _draw(_build_model(num))
