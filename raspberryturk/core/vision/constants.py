import cv2
import numpy as np

BOARD_SIZE = 800
SQUARE_SIZE = int(BOARD_SIZE / 8)

ROI = (350, 1350, 900, 2100)

top_left = [[95, 60]]  # bottom right[]y,x
bottom_left = [[18, 735]]  # bottom left
top_right = [[675, 83]]  # top right
bottom_right = [[730, 750]]  # y delta olnly first column
pts1 = np.float32([top_left, bottom_right, top_right, bottom_left, ])
pts2 = np.float32([[0, 0], [BOARD_SIZE, BOARD_SIZE], [BOARD_SIZE, 0], [0, BOARD_SIZE], ])
M = cv2.getPerspectiveTransform(pts1, pts2)
