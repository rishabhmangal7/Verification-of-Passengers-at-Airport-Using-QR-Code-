import pyqrcode
import png
from PIL import Image

content = "hello"
img = pyqrcode.create(content)
img.png("qrimg.png", scale=5)
img = Image.open("resource/Images/qrimg.png")
img.show()