from quart import abort

import boards


def validate_board(board: str) -> None:
    if board not in boards.boards:
        abort(404)


def validate_boards(board_names: str) -> None:
    for board_name in board_names:
        if board_name not in boards.boards:
            abort(404)


def validate_threads(threads: list[dict]):
    if len(threads) < 1:
        abort(404)


def validate_board_value_error(board: str) -> None:
    if board not in boards.boards:
        raise ValueError(board)
