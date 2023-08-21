import requests
import base64
import io
from PIL import Image
import pytesseract
# from cv2 import cv as cv
import cv2


def read_captcha(captcha_image_data):
    # Decode the image data from base64
    captcha_image_bytes = base64.b64decode(captcha_image_data)

    # Convert the image bytes to PIL Image object
    captcha_image = Image.open(io.BytesIO(captcha_image_bytes))

    # Display or save the CAPTCHA image, optional
    captcha_image.show()
    #Save the captcha image
    captcha_image.save('captcha_image.png')
    img = cv2.imread("captcha_image.png")
    gry = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    (h, w) = gry.shape[:2]
    gry = cv2.resize(gry, (w*2, h*2))
    cls = cv2.morphologyEx(gry, cv2.MORPH_CLOSE, None)
    thr = cv2.threshold(cls, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    return pytesseract.image_to_string(thr)