#coding:utf-8
# OCR识别中英文(无法下载训练库-_-)
import pytesseract
from PIL import Image


image = Image.open('./pic.png')
code = pytesseract.image_to_string(image)
print code
