import tkinter as tk
from PIL import Image, ImageTk

class FullScreenApp:
    def __init__(self, master):
        self.master = master
        master.title("Full Screen App")
        master.attributes('-fullscreen', True)
        master.config(bg="#6f70b3")  # Set the background color of the window

        # Bind the Esc key to close the app
        master.bind('<Escape>', lambda e: master.destroy())

        # Create a canvas to display the image
        self.canvas = tk.Canvas(master, bg="#6f70b3", highlightthickness=0)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # Load and resize the image
        self.load_image("image.jpg")

        # Bind a click event to the canvas
        self.canvas.bind('<Button-1>', self.canvas_clicked)
        
    def load_image(self, image_path):
        # Load the image
        original_image = Image.open(image_path)

        # Get the screen dimensions
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()

        # Resize the image while maintaining aspect ratio
        ratio = min(screen_width / original_image.width, screen_height / original_image.height)
        new_width = int(original_image.width * ratio)
        new_height = int(original_image.height * ratio)
        resized_image = original_image.resize((new_width, new_height))

        # Convert the resized image to Tkinter format
        self.image = ImageTk.PhotoImage(resized_image)

        # Display the image on the canvas
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.image)

    def canvas_clicked(self, event):
        # Check if the click coordinates are within the image boundaries
        if 0 <= event.x < self.image.width() and 0 <= event.y < self.image.height():
            print(f"Clicked on image at (x={event.x}, y={event.y})")

# Create the Tkinter root window
root = tk.Tk()

# Create the FullScreenApp instance
app = FullScreenApp(root)

# Run the Tkinter event loop
root.mainloop()
