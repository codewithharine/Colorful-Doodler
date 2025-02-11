import tkinter as tk
from tkinter import colorchooser, filedialog, simpledialog  # Import simpledialog
from PIL import Image, ImageDraw

class ColorfulDoodler:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Colorful Doodler ??")

        self.canvas_width = 400
        self.canvas_height = 400

        # Set up drawing canvas
        self.canvas = tk.Canvas(self.window, width=self.canvas_width, height=self.canvas_height, bg="white")
        self.canvas.pack()

        # Create an empty image for drawing
        self.image = Image.new("RGB", (self.canvas_width, self.canvas_height), "white")
        self.draw = ImageDraw.Draw(self.image)

        # Brush settings
        self.brush_color = "black"
        self.brush_size = 5

        # Bind mouse events
        self.canvas.bind("<B1-Motion>", self.paint)

        # Control Buttons
        button_frame = tk.Frame(self.window)
        button_frame.pack()

        color_button = tk.Button(button_frame, text="Pick Color", command=self.pick_color)
        color_button.pack(side=tk.LEFT)

        size_button = tk.Button(button_frame, text="Brush Size", command=self.pick_brush_size)
        size_button.pack(side=tk.LEFT)

        save_button = tk.Button(button_frame, text="Save Doodle", command=self.save_doodle)
        save_button.pack(side=tk.LEFT)

        clear_button = tk.Button(button_frame, text="Clear Canvas", command=self.clear_canvas)
        clear_button.pack(side=tk.LEFT)

        self.window.mainloop()

    def paint(self, event):
        # Draw on the canvas and PIL image
        x1, y1 = event.x - self.brush_size, event.y - self.brush_size
        x2, y2 = event.x + self.brush_size, event.y + self.brush_size
        self.canvas.create_oval(x1, y1, x2, y2, fill=self.brush_color, outline=self.brush_color)
        self.draw.ellipse([x1, y1, x2, y2], fill=self.brush_color)

    def pick_color(self):
        # Open color picker dialog
        color = colorchooser.askcolor()[1]
        if color:
            self.brush_color = color

    def pick_brush_size(self):
        # Ask for brush size
        size = simpledialog.askinteger("Brush Size", "Enter brush size (1-20):", minvalue=1, maxvalue=20)
        if size:
            self.brush_size = size

    def save_doodle(self):
        # Save the current image to file
        file_path = filedialog.asksaveasfilename(defaultextension=".png",
                                                  filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
        if file_path:
            self.image.save(file_path)

    def clear_canvas(self):
        # Clear the canvas and reset the PIL image
        self.canvas.delete("all")
        self.image = Image.new("RGB", (self.canvas_width, self.canvas_height), "white")
        self.draw = ImageDraw.Draw(self.image)

# Run the app
ColorfulDoodler()
