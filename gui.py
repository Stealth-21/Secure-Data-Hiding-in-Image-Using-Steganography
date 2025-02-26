import tkinter as tk
from tkinter import filedialog, messagebox
from encode_lsb import encode_lsb
from decode_lsb import decode_lsb

def run_gui():
    def open_file():
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.bmp")])
        if file_path:
            entry_image_path.delete(0, tk.END)
            entry_image_path.insert(0, file_path)

    def encode_data():
        image_path = entry_image_path.get()
        data = entry_data.get()
        apply_grayscale = grayscale_var.get()
        apply_blur = blur_var.get()
        if image_path and data:
            try:
                encoded_image_path = encode_lsb(image_path, data, apply_grayscale, apply_blur)
                messagebox.showinfo("Success", f"Data encoded in {encoded_image_path}")
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {e}")

    def decode_data():
        image_path = entry_image_path.get()
        if image_path:
            try:
                decoded_message = decode_lsb(image_path)
                messagebox.showinfo("Decoded Message", decoded_message)
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {e}")

    root = tk.Tk()
    root.title("Steganography Tool")

    tk.Label(root, text="Image Path:").pack()
    entry_image_path = tk.Entry(root, width=50)
    entry_image_path.pack()

    tk.Button(root, text="Browse", command=open_file).pack()

    tk.Label(root, text="Data to Encode (max 128 chars):").pack()
    entry_data = tk.Entry(root, width=50)
    entry_data.pack()

    grayscale_var = tk.BooleanVar()
    blur_var = tk.BooleanVar()

    tk.Checkbutton(root, text="Apply Grayscale", variable=grayscale_var).pack()
    tk.Checkbutton(root, text="Apply Blur", variable=blur_var).pack()

    tk.Button(root, text="Encode", command=encode_data).pack()
    tk.Button(root, text="Decode", command=decode_data).pack()

    root.mainloop()