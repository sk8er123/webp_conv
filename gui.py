from tkinter import Tk, Frame, Button, Listbox, Entry, Label, filedialog, messagebox
from PIL import Image

class WebPConverterGUI:
    def __init__(self, root):
        self.root = root
        root.title("WebP Animation Creator")

        self.frame = Frame(root)
        self.frame.pack(padx=10, pady=10)

        self.select_button = Button(self.frame, text="Select Images", command=self.select_images)
        self.select_button.pack(pady=5)

        self.listbox = Listbox(self.frame, width=100, height=10)
        self.listbox.pack(pady=5)

        self.clear_button = Button(self.frame, text="Clear", command=self.clear_selection)
        self.clear_button.pack(pady=5)

        self.label_filename = Label(self.frame, text="Output File Name:")
        self.label_filename.pack(pady=5)

        self.filename_entry = Entry(self.frame, width=48)
        self.filename_entry.pack(pady=5)
        self.filename_entry.insert(0, "output_animation.webp")  # Default file name

        self.label_quality = Label(self.frame, text="Quality (0-100):")
        self.label_quality.pack(pady=5)

        self.quality_entry = Entry(self.frame, width=48)
        self.quality_entry.pack(pady=5)
        self.quality_entry.insert(0, "80")  # Default quality value

        self.label_duration = Label(self.frame, text="Duration (milliseconds):")
        self.label_duration.pack(pady=5)

        self.duration_entry = Entry(self.frame, width=48)
        self.duration_entry.pack(pady=5)
        self.duration_entry.insert(0, "100")  # Default duration value

        self.convert_button = Button(self.frame, text="Convert to WebP", command=self.convert_to_webp)
        self.convert_button.pack(pady=5)

        self.selected_files = []

    def select_images(self):
        file_paths = filedialog.askopenfilenames(title="Select images", filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
        for file_path in file_paths:
            self.listbox.insert('end', file_path)
        self.selected_files += file_paths

    def clear_selection(self):
        self.listbox.delete(0, 'end')
        self.selected_files = []

    def convert_to_webp(self):
        if not self.selected_files:
            messagebox.showwarning("Warning", "No files selected!")
            return

        output_filename = self.filename_entry.get()
        if not output_filename:
            messagebox.showwarning("Warning", "Output file name is required!")
            return

        try:
            quality = int(self.quality_entry.get())
            if not 0 <= quality <= 100:
                raise ValueError("Quality must be between 0 and 100.")
        except ValueError as e:
            messagebox.showerror("Error", f"Invalid quality value: {e}")
            return

        try:
            duration = int(self.duration_entry.get())
            if duration <= 0:
                raise ValueError("Duration must be greater than 0.")
        except ValueError as e:
            messagebox.showerror("Error", f"Invalid duration value: {e}")
            return

        base_image = Image.open(self.selected_files[0])
        image_sequence = [Image.open(img).convert("RGBA") for img in self.selected_files[1:]]
        base_image.save(output_filename, save_all=True, append_images=image_sequence, loop=0, duration=duration, quality=quality)
        messagebox.showinfo("Success", f"Conversion to {output_filename} completed!")

if __name__ == "__main__":
    root = Tk()
    app = WebPConverterGUI(root)
    root.mainloop()
