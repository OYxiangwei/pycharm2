from PIL import Image
import pytesseract as pt

image = Image.open('')
s = pt.image_to_string(image)
print(s)