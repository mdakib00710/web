
import numpy as np
import cv2
from PIL import Image

class EraseScratches:
    def erase(self, pil_image):
        # Dummy scratch removal: apply Gaussian blur
        np_img = np.array(pil_image)
        restored = cv2.GaussianBlur(np_img, (5, 5), 0)
        return restored
