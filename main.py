import logging
import PIL.Image

from zeroscratches import EraseScratches

logging.basicConfig(level=logging.INFO)

image_path = "0_Fu9ycPuy2M_gjj5R.jpg"
eraser = EraseScratches()

image = PIL.Image.open(image_path)
new_img = eraser.erase(image)

new_img = PIL.Image.fromarray(new_img)
new_img.show()
