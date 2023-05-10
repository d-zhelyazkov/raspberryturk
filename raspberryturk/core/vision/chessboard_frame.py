import cv2
import numpy as np

from . import img_diff
from .constants import SQUARE_SIZE, BOARD_SIZE, M, ROI, ROTATION
from .square import Square


class ChessboardFrame():
    def __init__(self, img):
        self.img = img

    def square_at(self, i):
        y = BOARD_SIZE - (int(i / 8) % 8) * SQUARE_SIZE - SQUARE_SIZE
        x = (i % 8) * SQUARE_SIZE
        return Square(i, self.img[y:y + SQUARE_SIZE, x:x + SQUARE_SIZE])


def get(img_read):
    img_roi = img_read[ROI[0]:ROI[1], ROI[2]:ROI[3]]
    img_captured = cv2.resize(img_roi, (BOARD_SIZE, BOARD_SIZE))
    warped = cv2.warpPerspective(img_captured, M, (BOARD_SIZE, BOARD_SIZE))
    img = cv2.rotate(warped, ROTATION)
    return img


def move_cells(board_1, board_2):
    img_diff_ = img_diff(board_1, board_2)
    frame_diff = ChessboardFrame(img_diff_)
    cell_diffs = [
        frame_diff.square_at(cell).raw_img.sum()
        for cell in range(64)
    ]
    return np.argsort(cell_diffs)[-2:]
