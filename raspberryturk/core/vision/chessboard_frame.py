import cv2

from .constants import SQUARE_SIZE, BOARD_SIZE, M, ROI
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
    return ChessboardFrame(warped)
