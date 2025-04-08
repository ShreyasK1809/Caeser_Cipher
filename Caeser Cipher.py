import tkinter as tk
from tkinter import messagebox

# Caesar Cipher Logic
def caesar_cipher_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            encrypted_text += chr((ord(char) - start + shift) % 26 + start)
        else:
            encrypted_text += char
    return encrypted_text


def caesar_cipher_decrypt(text, shift):
    return caesar_cipher_encrypt(text, -shift)


# GUI Application Class
class CaesarCipherApp:
    def __init__(self, master):
        self.master = master
        master.title("Caesar Cipher GUI")
        master.geometry("400x350")
        master.config(padx=20, pady=20)

        # Input Label and Textbox
        self.label_input = tk.Label(master, text="Enter your message:")
        self.label_input.pack()
        self.text_input = tk.Text(master, height=3, width=40)
        self.text_input.pack(pady=5)

        # Shift Value
        self.label_shift = tk.Label(master, text="Enter shift value:")
        self.label_shift.pack()
        self.shift_input = tk.Entry(master)
        self.shift_input.pack(pady=5)

        # Encrypt and Decrypt Buttons
        self.encrypt_button = tk.Button(master, text="Encrypt", command=self.encrypt_text)
        self.encrypt_button.pack(pady=5)

        self.decrypt_button = tk.Button(master, text="Decrypt", command=self.decrypt_text)
        self.decrypt_button.pack(pady=5)

        # Result Label and Textbox
        self.label_result = tk.Label(master, text="Result:")
        self.label_result.pack()
        self.text_result = tk.Text(master, height=3, width=40, state='disabled')
        self.text_result.pack(pady=5)

    def encrypt_text(self):
        try:
            shift = int(self.shift_input.get())
            message = self.text_input.get("1.0", tk.END).strip()
            encrypted = caesar_cipher_encrypt(message, shift)
            self.display_result(encrypted)
        except ValueError:
            messagebox.showerror("Invalid Input", "Shift value must be an integer.")

    def decrypt_text(self):
        try:
            shift = int(self.shift_input.get())
            message = self.text_input.get("1.0", tk.END).strip()
            decrypted = caesar_cipher_decrypt(message, shift)
            self.display_result(decrypted)
        except ValueError:
            messagebox.showerror("Invalid Input", "Shift value must be an integer.")

    def display_result(self, result):
        self.text_result.config(state='normal')
        self.text_result.delete("1.0", tk.END)
        self.text_result.insert(tk.END, result)
        self.text_result.config(state='disabled')


# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = CaesarCipherApp(root)
    root.mainloop()