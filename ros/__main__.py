#!/usr/bin/env python3

import logging
from datetime import datetime

import cv2
import roslibpy
from roslibpy import Topic

from core import opencv, mkdir
from core.game.stockfish_player import StockfishPlayer
from core.vision import chessboard_frame
from embedded import game

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

IMG_DIR = mkdir("images/")

ros = roslibpy.Ros(host='localhost', port=9090)

moves = Topic(ros, '/move_ack', 'std_msgs/Empty')
changed_cells = Topic(ros, '/changed_cells', 'std_msgs/String')
next_moves = Topic(ros, '/next_move', 'std_msgs/String')
errors = Topic(ros, '/error', 'std_msgs/String')

camera = opencv.Camera()
AI = StockfishPlayer()


def get_board_img():
    ts = datetime.now().strftime('%Y%m%d_%H%M%S')

    raw_img = camera.frame
    cv2.imwrite(str(IMG_DIR / f"{ts}_raw.png"), raw_img)

    img = chessboard_frame.get(raw_img)
    cv2.imwrite(str(IMG_DIR / f"{ts}.png"), img)

    return img


board_img = get_board_img()
game.start_new_game()


def publish(topic: Topic, msg):
    topic.publish(roslibpy.Message({'data': msg}))


def update_game(_):
    try:
        global board_img

        new_board_img = get_board_img()
        _changed_cells = game.cells_strs(
            chessboard_frame.move_cells(board_img, new_board_img))
        publish(changed_cells, str(_changed_cells))
        log.info(f"Detected cells: {_changed_cells}")

        game.apply_move(game.move(_changed_cells))
        board_img = new_board_img
        log.info(f"Updated board:\n{game.get_board()}")

        recommend_next_move()

    except ValueError as e:
        # invalid move, etc...
        log.error("Error updating game...", exc_info=e)
        publish(errors, str(e))


def recommend_next_move():
    board = game.get_board()
    move = AI.select_move(board)

    from_cell = game.cell_str(move.from_square).upper()
    to_cell = game.cell_str(move.to_square).upper()
    move_seq = (f"{from_cell}-{to_cell}",)

    capture_piece = board.piece_at(move.to_square)
    if capture_piece:
        move_seq = (f"{to_cell}-*",) + move_seq

    # TODO: promotion and castle moves support

    publish(next_moves, ','.join(move_seq))


moves.subscribe(update_game)

log.info("Initialized!")
# client.run()
ros.run_forever()

# try:
#     while True:
#         pass
# except Exception:
#     client.terminate()
#     camera.__exit__()
