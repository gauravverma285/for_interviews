

# program for ocr means extract the text from image

# from PIL import Image
# import pytesseract
# import numpy as np
# from pytesseract import Output
# import cv2

# pytesseract.pytesseract.tesseract_cmd =r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# filename = '1.png'
# img = np.array(Image.open(filename))
# text = pytesseract.image_to_string(img)

# print(text, 'AAAAAAAAAAAAAAAAA')

from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

filename = '1.png'
img = Image.open(filename)
text = pytesseract.image_to_string(img)

print(text, 'AAAAAAAAAAAA')


# a , b = 0 , 1

# while a < 10:
#     print(a)
#     a,b = b, a+b
#     print(a , b, "AAAAAAAAAAAAA")


# 1: global and local variable
# 2: mutable -- list, dict, sets
# 3: immutable -- str, int, float, tuple
# 4: list , dict, opration
# 5: and , or and not operator
# 6: pass, continue, break
# 7: interpreted language

# 8: lambda function
# 9: decorator
# 10: build-in datatypes -- The 5 built-in data types in Python are: None Type, 
#                             Numeric Types (int, float, complex, bool), 
#                             Sequence Types (list, tuple, range, str),     

#                             Map Type (dictionary), 
#                             and Set types (set, frozenset).

# 11: indexing and negative indexing
# 12: what is self in python
# 13: oops concept
# 14: slicing in python
# 15: file handling