import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image

class ImageConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("JPEG to PNG Converter")
        self.root.configure(bg='#f4f4f4')  # Light gray background
        self.im = None  # Image holder

        self.setup_ui()

    def setup_ui(self):
        canvas = tk.Canvas(self.root, width=300, height=250, bg='#f4f4f4', highlightthickness=0)
        canvas.pack()

        title_label = tk.Label(self.root, text="File Converter", bg='#e0f7fa', fg='#00695c', font=('helvetica', 20, 'bold'))
        canvas.create_window(150, 60, window=title_label)

        self.create_button(canvas, "Import JPEG File", self.load_image, 130)
        self.create_button(canvas, "Convert to PNG", self.save_image, 180)

    def create_button(self, canvas, text, command, y_pos):
        button = tk.Button(
            self.root,
            text=text,
            command=command,
            bg='#00897b',       # Teal
            fg='white',
            activebackground='#004d40',
            font=('helvetica', 12, 'bold'),
            relief='raised',
            bd=3
        )
        canvas.create_window(150, y_pos, window=button)

    def load_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("JPEG files", "*.jpg;*.jpeg")])
        if file_path:
            self.im = Image.open(file_path)

    def save_image(self):
        if self.im is None:
            messagebox.showerror("Error", "No file selected.")
            return
        save_path = filedialog.asksaveasfilename(defaultextension='.png', filetypes=[("PNG files", "*.png")])
        if save_path:
            self.im.save(save_path)

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = ImageConverterApp(root)
    root.mainloop()
