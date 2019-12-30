from PIL import Image
from pytesseract import image_to_string



img=Image.open('/Users/sambitmallick/Downloads/img2.png')

text=image_to_string(img)
print(text)