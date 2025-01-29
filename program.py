import tkinter as tk
import random
from PIL import Image, ImageTk

# File paths for images
ASK_IMG_PATH = "D:/Hack Club/Project 37/ask.png"
YES_IMG_PATH = "D:/Hack Club/Project 37/yes.gif"

class LoveApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Do You Love Me?")
        self.root.configure(bg="#ffafbd")
        
        # Set window size to 60% of screen width and height
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        window_width = int(screen_width * 0.6)
        window_height = int(screen_height * 0.6)
        root.geometry(f"{window_width}x{window_height}")
        
        # Wrapper frame for UI elements
        self.wrapper = tk.Frame(root, bg="white", padx=30, pady=20)
        self.wrapper.pack(expand=True, fill="both")
        
        # Question label
        self.question_label = tk.Label(self.wrapper, text="Do you love me?", font=("Poppins", 24, "bold"), bg="white", fg="#333")
        self.question_label.pack(pady=20)
        
        # Load images
        self.ask_img = self.load_image(ASK_IMG_PATH)
        self.yes_img = self.load_image(YES_IMG_PATH)
        
        # GIF label
        self.gif_label = tk.Label(self.wrapper, image=self.ask_img, bg="white")
        self.gif_label.pack(pady=20)
        
        # Button frame
        self.button_frame = tk.Frame(self.wrapper, bg="white")
        self.button_frame.pack(pady=20)
        
        # Yes button
        self.yes_button = tk.Button(self.button_frame, text="Yes", font=("Poppins", 18, "bold"), 
                                    bg="#4caf50", fg="white", padx=30, pady=12, command=self.on_yes_click)
        self.yes_button.pack(side="left", padx=10)
        
        # No button (Initially placed next to Yes button)
        self.no_button = tk.Button(self.button_frame, text="No", font=("Poppins", 18, "bold"), 
                                   bg="#ff4d4d", fg="white", padx=30, pady=12, command=self.reset_no_button)
        self.no_button.pack(side="left", padx=10)
        self.no_button.bind("<Enter>", self.on_no_hover)
    
    def load_image(self, path, size=(250, 250)):
        """Loads and resizes an image from the given path."""
        try:
            img = Image.open(path)
            img = img.resize(size, Image.Resampling.LANCZOS)
            return ImageTk.PhotoImage(img)
        except Exception as e:
            print(f"Error loading image {path}: {e}")
            return None
    
    def on_yes_click(self):
        """Handles the Yes button click event."""
        self.question_label.config(text="Being with you is my biggest blessing. I love you ❤️")
        self.gif_label.config(image=self.yes_img)
        self.yes_button.pack_forget()
        self.no_button.place_forget()
    
    def on_no_hover(self, event):
        """Moves the No button randomly within screen bounds when hovered over."""
        if self.no_button.winfo_ismapped():
            max_x = self.wrapper.winfo_width() - self.no_button.winfo_width()
            max_y = self.wrapper.winfo_height() - self.no_button.winfo_height()
            x = random.randint(10, max_x)
            y = random.randint(10, max_y)
            self.no_button.place(x=x, y=y)
    
    def reset_no_button(self):
        """Recreates the No button in a new random position after being clicked."""
        self.no_button.pack_forget()
        max_x = self.wrapper.winfo_width() - self.no_button.winfo_width()
        max_y = self.wrapper.winfo_height() - self.no_button.winfo_height()
        x = random.randint(10, max_x)
        y = random.randint(10, max_y)
        self.no_button.place(x=x, y=y)

if __name__ == "__main__":
    root = tk.Tk()
    app = LoveApp(root)
    root.mainloop()
