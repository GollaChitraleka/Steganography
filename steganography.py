import cv2
import os
import tkinter as tk
from tkinter import messagebox, filedialog
from tkinter import ttk

# Global variables to store encryption state
global_img = None
global_msg = ""
global_password = ""

def encrypt_action():
    global global_img, global_msg, global_password
    # Ask the user to select an image for encryption
    img_path = filedialog.askopenfilename(
        title="Select an Image for Encryption", 
        filetypes=[("Image Files", "*.jpg;*.jpeg;*.png")]
    )
    if not img_path:
        messagebox.showerror("Error", "No image selected!")
        return
    
    global_img = cv2.imread(img_path)
    if global_img is None:
        messagebox.showerror("Error", "Image could not be read!")
        return
    
    # Get secret message and passcode from GUI entries
    global_msg = message_entry.get()
    global_password = password_entry.get()
    
    if not global_msg or not global_password:
        messagebox.showerror("Error", "Secret message and passcode required!")
        return

    # Create character mappings (unchanged logic)
    d = {}
    c = {}
    for i in range(255):
        d[chr(i)] = i
        c[i] = chr(i)

    m = 0
    n = 0
    z = 0

    # Encrypt the message into the image
    for i in range(len(global_msg)):
        global_img[n, m, z] = d[global_msg[i]]
        n = n + 1
        m = m + 1
        z = (z + 1) % 3

    # Save the encrypted image (using PNG to avoid lossy compression)
    encrypted_path = "encryptedImage.png"
    cv2.imwrite(encrypted_path, global_img)
    os.system(f"start {encrypted_path}")  # Open the image on Windows
    messagebox.showinfo("Success", "Message encrypted successfully!\nUse the same encrypted image for decryption.")

def decrypt_action():
    # Get passcode for decryption from GUI entry
    pas = decryption_password_entry.get()
    if global_password == pas:
        # Ask the user to select the encrypted image for decryption
        img_path = filedialog.askopenfilename(
            title="Select the Encrypted Image for Decryption", 
            filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")]
        )
        if not img_path:
            messagebox.showerror("Error", "No image selected!")
            return
        
        de_img = cv2.imread(img_path)
        if de_img is None:
            messagebox.showerror("Error", "Image could not be read!")
            return
        
        # Create character mappings (unchanged logic)
        d = {}
        c = {}
        for i in range(255):
            d[chr(i)] = i
            c[i] = chr(i)
        
        message = ""
        n = 0
        m = 0
        z = 0

        # Decrypt the message from the selected encrypted image using the length of the original message
        for i in range(len(global_msg)):
            message = message + c[de_img[n, m, z]]
            n = n + 1
            m = m + 1
            z = (z + 1) % 3
        messagebox.showinfo("Decryption", f"Decryption message: {message}")
    else:
        messagebox.showerror("Error", "YOU ARE NOT auth")

# GUI Setup
root = tk.Tk()
root.title("Image Steganography")
root.geometry("500x400")
root.configure(bg="#f0f0f0")

# Use ttk for styling
style = ttk.Style(root)
style.theme_use('clam')
style.configure("TLabel", background="#f0f0f0", foreground="#333", font=("Helvetica", 12))
style.configure("TButton", background="#007acc", foreground="#fff", font=("Helvetica", 12), padding=6)
style.map("TButton", background=[("active", "#005f99")])
style.configure("TEntry", font=("Helvetica", 12), padding=4)
style.configure("TLabelframe", background="#f0f0f0", font=("Helvetica", 12, "bold"))
style.configure("TLabelframe.Label", background="#f0f0f0", foreground="#007acc")

# Title Label
title_label = ttk.Label(root, text="Image Steganography", font=("Helvetica", 16, "bold"))
title_label.pack(pady=10)

# Encryption section
encrypt_frame = ttk.LabelFrame(root, text="Encryption", padding=(20, 10))
encrypt_frame.pack(pady=10, padx=20, fill="x")

secret_msg_label = ttk.Label(encrypt_frame, text="Enter secret message:")
secret_msg_label.pack(anchor="w", pady=5)
message_entry = ttk.Entry(encrypt_frame, width=50)
message_entry.pack(pady=5)

passcode_label = ttk.Label(encrypt_frame, text="Enter a passcode:")
passcode_label.pack(anchor="w", pady=5)
password_entry = ttk.Entry(encrypt_frame, width=50, show="*")
password_entry.pack(pady=5)

encrypt_button = ttk.Button(encrypt_frame, text="Encrypt", command=encrypt_action)
encrypt_button.pack(pady=10)

# Decryption section
decrypt_frame = ttk.LabelFrame(root, text="Decryption", padding=(20, 10))
decrypt_frame.pack(pady=10, padx=20, fill="x")

decryption_passcode_label = ttk.Label(decrypt_frame, text="Enter passcode for Decryption:")
decryption_passcode_label.pack(anchor="w", pady=5)
decryption_password_entry = ttk.Entry(decrypt_frame, width=50, show="*")
decryption_password_entry.pack(pady=5)

decrypt_button = ttk.Button(decrypt_frame, text="Decrypt", command=decrypt_action)
decrypt_button.pack(pady=10)

root.mainloop()
