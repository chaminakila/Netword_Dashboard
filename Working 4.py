import tkinter as tk
from PIL import Image, ImageTk
import json

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

        # Draw and start blinking the circles
        self.draw_and_blink_circles()
        
        # Draw transparent squares with an outline
        self.draw_squares()

        # Bind a click event to the canvas
        self.canvas.bind('<Button-1>', self.canvas_clicked)
        
        # Create buttons with icons
        self.create_buttons()

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

    def draw_squares(self):
        # Define the coordinates of the squares
        square1_x1 = 0.314787701317716*self.master.winfo_screenwidth()  # Adjust the x-coordinate of the top-left corner of square1
        square1_y1 = 0.0690104166666667*self.master.winfo_screenheight()  # Adjust the y-coordinate of the top-left corner of square1
        square1_x2 = 0.4707174231332357*self.master.winfo_screenwidth()  # Adjust the x-coordinate of the bottom-right corner of square1
        square1_y2 = 0.1783854166666667*self.master.winfo_screenheight()  # Adjust the y-coordinate of the bottom-right corner of square1

        square2_x1 = 0.6010248901903367*self.master.winfo_screenwidth()  # Adjust the x-coordinate of the top-left corner of square2
        square2_y1 = 0.0651041666666667*self.master.winfo_screenheight()  # Adjust the y-coordinate of the top-left corner of square2
        square2_x2 = 0.6756954612005857*self.master.winfo_screenwidth()  # Adjust the x-coordinate of the bottom-right corner of square2
        square2_y2 = 0.1979166666666667*self.master.winfo_screenheight()  # Adjust the y-coordinate of the bottom-right corner of square2

        square3_x1 = 0.7518301610541728*self.master.winfo_screenwidth()  # Adjust the x-coordinate of the top-left corner of square3
        square3_y1 = 0.33203125*self.master.winfo_screenheight()  # Adjust the y-coordinate of the top-left corner of square3
        square3_x2 = 0.9150805270863836*self.master.winfo_screenwidth()  # Adjust the x-coordinate of the bottom-right corner of square3
        square3_y2 = 0.4296875*self.master.winfo_screenheight()  # Adjust the y-coordinate of the bottom-right corner of square3

        square4_x1 = 0.5417276720351391*self.master.winfo_screenwidth()  # Adjust the x-coordinate of the top-left corner of square4
        square4_y1 = 0.3372395833333333*self.master.winfo_screenheight()  # Adjust the y-coordinate of the top-left corner of square4
        square4_x2 = 0.6705710102489019*self.master.winfo_screenwidth()  # Adjust the x-coordinate of the bottom-right corner of square4
        square4_y2 = 0.4127604166666667*self.master.winfo_screenheight()  # Adjust the y-coordinate of the bottom-right corner of square4

        square5_x1 = 0.2759882869692533*self.master.winfo_screenwidth()  # Adjust the x-coordinate of the top-left corner of square5
        square5_y1 = 0.3515625*self.master.winfo_screenheight()  # Adjust the y-coordinate of the top-left corner of square5
        square5_x2 = 0.4275256222547584*self.master.winfo_screenwidth()  # Adjust the x-coordinate of the bottom-right corner of square5
        square5_y2 = 0.40234375*self.master.winfo_screenheight()  # Adjust the y-coordinate of the bottom-right corner of square5

        # Draw the squares with transparent fill and an outline
        self.square1 = self.canvas.create_rectangle(square1_x1, square1_y1, square1_x2, square1_y2, outline="")
        self.square2 = self.canvas.create_rectangle(square2_x1, square2_y1, square2_x2, square2_y2, outline="")
        self.square3 = self.canvas.create_rectangle(square3_x1, square3_y1, square3_x2, square3_y2, outline="")
        self.square4 = self.canvas.create_rectangle(square4_x1, square4_y1, square4_x2, square4_y2, outline="")
        self.square5 = self.canvas.create_rectangle(square5_x1, square5_y1, square5_x2, square5_y2, outline="")

    def canvas_clicked(self, event):
        # Check if the click coordinates are within the square's boundaries
        square1_bbox = self.canvas.bbox(self.square1)
        square2_bbox = self.canvas.bbox(self.square2)
        square3_bbox = self.canvas.bbox(self.square3)
        square4_bbox = self.canvas.bbox(self.square4)
        square5_bbox = self.canvas.bbox(self.square5)
        
        if square1_bbox[0] <= event.x <= square1_bbox[2] and square1_bbox[1] <= event.y <= square1_bbox[3]:
            print("Square 1 clicked!")
        elif square2_bbox[0] <= event.x <= square2_bbox[2] and square2_bbox[1] <= event.y <= square2_bbox[3]:
            print("Square 2 clicked!")
        elif square3_bbox[0] <= event.x <= square3_bbox[2] and square3_bbox[1] <= event.y <= square3_bbox[3]:
            print("Square 3 clicked!")
        elif square4_bbox[0] <= event.x <= square4_bbox[2] and square4_bbox[1] <= event.y <= square4_bbox[3]:
            print("Square 4 clicked!")
        elif square5_bbox[0] <= event.x <= square5_bbox[2] and square5_bbox[1] <= event.y <= square5_bbox[3]:
            print("Square 5 clicked!")

    def draw_and_blink_circles(self):
        # Define circle coordinates, sizes, and colors
        circles = [
            {"center_x": 442, "center_y": 125, "radius": 10},
            {"center_x": 833, "center_y": 140, "radius": 10},
            {"center_x": 1039, "center_y": 319, "radius": 10},
            {"center_x": 751, "center_y": 305, "radius": 10},
            {"center_x": 389, "center_y": 297, "radius": 10}
        ]

        # Draw each circle with outline and color based on initial data
        self.circles = []
        for i, circle_data in enumerate(circles):
            color = "#00ff00"  # Initial color
            circle = self.canvas.create_oval(
                circle_data["center_x"] - circle_data["radius"],
                circle_data["center_y"] - circle_data["radius"],
                circle_data["center_x"] + circle_data["radius"],
                circle_data["center_y"] + circle_data["radius"],
                fill=color, outline="black"
            )
            self.circles.append(circle)

        # Start blinking the circles
        self.blink_circles()

    def blink_circles(self):
        # Load data from data.json before blinking
        self.load_data("data.json")

        for i, circle in enumerate(self.circles):
            # Update circle color based on active state in data.json
            color = "#00ff00" if self.data["switches"][i]["active_state"] else "#ff0000"
            self.canvas.itemconfigure(circle, fill=color)

        for circle in self.circles:
            # Toggle the visibility of each circle
            current_state = self.canvas.itemcget(circle, "state")
            new_state = "hidden" if current_state == "normal" else "normal"
            self.canvas.itemconfigure(circle, state=new_state)

        # Schedule the next blink for circles after 1 second
        self.master.after(1000, self.blink_circles)

    def load_data(self, file_path):
        # Load data from JSON file
        with open(file_path, 'r') as file:
            self.data = json.load(file)

    def create_buttons(self):
        # Create buttons with icons
        icon_files = ["back.jpg", "playpause.jpg", "next.jpg", "settings.jpg"]
        button_width = 40  # Adjust button width as needed
        button_height = 40  # Adjust button height as needed
        button_margin = 20  # Adjust button margin as needed

        total_button_width = (button_width + button_margin) * len(icon_files) - button_margin
        start_x = (self.master.winfo_screenwidth() - total_button_width) // 2  # Center the buttons horizontally

        for i, icon_file in enumerate(icon_files):
            icon_image = Image.open(icon_file)
            icon_image = icon_image.resize((32, 32))  # Resize the icon image as needed
            icon_tk = ImageTk.PhotoImage(icon_image)

            button = tk.Button(self.master, image=icon_tk, bg="#4CAF50", fg="white", width=button_width, height=button_height)
            button.image = icon_tk  # Keep a reference to the image to prevent garbage collection
            button.place(x=start_x + i * (button_width + button_margin), y=self.master.winfo_screenheight() - 50 - button_height)

# Create the Tkinter root window
root = tk.Tk()

# Create the FullScreenApp instance
app = FullScreenApp(root)

# Run the Tkinter event loop
root.mainloop()
