from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
import subprocess
from .ocr import run_ocr_on_image
from .detect_scanner import check_printer
from django.contrib.auth.decorators import login_required

# This function will check if the printer is connected
@login_required
def check_printered(request):
    print("User authenticated:", request.user.is_authenticated)
    printer_found = check_printer()  # Use your printer detection logic here

    context = {'printer_found': printer_found}
    return render(request, 'index.html', context)

# This function will handle the scanning process and run OCR
def scan_and_ocr(request):
    if request.method == 'POST':
        # Trigger scanning process (replace with your scanner's command)
        subprocess.run(['scanimage', '--format=png', '--mode=color','-o', 'scanned_image.png'])
        
        # Run OCR on the scanned image
        extracted_text = run_ocr_on_image('scanned_image.png')
        
        context = {'extracted_text': extracted_text, 'scanned_image': 'scanned_image.png'}
        return render(request, 'ocr_result.html', context)

    return render(request, 'index.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
    return render(request, 'registration/login.html')

def user_logout(request):
    logout(request)
    return redirect('login')
