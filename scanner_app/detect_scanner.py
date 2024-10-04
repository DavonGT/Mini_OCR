import subprocess

def check_printer():
    try:
        output = subprocess.check_output(['lpstat', '-p'])
        return True if output else False
    except subprocess.CalledProcessError:
        return False
