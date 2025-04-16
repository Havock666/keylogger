import tkinter as tk
from tkinter import filedialog, messagebox
from cryptography.fernet import Fernet

def decrypt_file():
    try:
        # Let user select the key file (.key)
        key_path = filedialog.askopenfilename(title="Select Key File (.key)", filetypes=[("Key Files", "*.key")])
        # Let user select the encrypted log (.encrypted)
        enc_path = filedialog.askopenfilename(title="Select Encrypted Log (.encrypted)", filetypes=[("Encrypted Logs", "*.encrypted")])

        # Load the encryption key
        with open(key_path, 'rb') as key_file:
            key = key_file.read()
        fernet = Fernet(key)

        # Read the encrypted log and decrypt
        with open(enc_path, 'rb') as enc_file:
            encrypted_data = enc_file.read()
        decrypted_data = fernet.decrypt(encrypted_data)

        # Let user choose location to save the decrypted log
        save_path = filedialog.asksaveasfilename(title="Save Decrypted Log As", defaultextension=".txt")
        with open(save_path, 'wb') as out_file:
            out_file.write(decrypted_data)

        messagebox.showinfo("Success", "Decryption completed successfully.")
    except Exception as e:
        messagebox.showerror("Error", f"Decryption failed:\n{e}")

# GUI Initialization
root = tk.Tk()
root.title("Keylog Decryptor")
root.geometry("300x150")

# Layout
tk.Button(root, text="Decrypt Keylog", command=decrypt_file, padx=20, pady=10).pack(pady=30)

root.mainloop()
