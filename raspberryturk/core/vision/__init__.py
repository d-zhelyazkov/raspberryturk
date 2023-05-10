import numpy as np


def img_diff(img1, img2):
    return np.uint8(np.abs(
        np.int16(img1) - img2
    ))
