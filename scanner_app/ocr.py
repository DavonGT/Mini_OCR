import pytesseract
from PIL import Image

def run_ocr_on_image(image_path):
    # Open the image
    img = Image.open(image_path)
    
    # Use pytesseract to extract text
    text = pytesseract.image_to_string(img)
    
    return text
