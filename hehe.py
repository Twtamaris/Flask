import os

def is_venv():
    return 'VIRTUAL_ENV' in os.environ

if is_venv():
    print("Virtual environment is activated.")
else:
    print("Virtual environment is not activated.")
