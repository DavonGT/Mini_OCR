# Django OCR & Printer Detection Web App

This is a Django web application that includes user registration and login functionalities. The main page features a scan button that only appears if a USB printer is detected. When clicked, it prompts the user to scan a form, and the scanned image is used as input for an OCR Python script to extract text from the image.

## Features

- User registration and login
- Logout button on the main page
- Printer detection (USB)
- Scanning in color
- OCR to extract text from scanned forms

## Requirements

### Software
- **Python 3.6+**
- **Django 3.x+**
- **CUPS (Common UNIX Printing System)** for printer detection
    sudo apt-get install cups
- **SANE (Scanner Access Now Easy)** for scanning images
    sudo apt-get install sane sane-utils
- **Tesseract OCR** for text extraction from scanned images
    sudo apt-get install tesseract-ocr

### Python Packages
You can install the required Python packages by running the following command:

```bash
pip install -r requirements.txt
