from tkinter import *
from tkinter.colorchooser import askcolor

class WhiteboardApp:
    def __init__(self, root):
        self.root = root
        self.colour = "blue"  # Default drawing color
        self.x0, self.y0 = 0, 0  # Initial mouse cursor position
        self.eraser_mode = False
        self.eraser_color = "White"
        self.canvas_width = 1040
        self.canvas_height = 2160
        self.create_widgets()

    def create_widgets(self):
        # Create scale widget for adjusting line width
        self.s1 = Scale(self.root, from_=1, to=25, orient=HORIZONTAL)
        self.s1.pack(anchor="n", ipadx=840, side="top")

        # Create canvas widget for drawing
        self.canvas = Canvas(self.root, width=self.canvas_width, height=self.canvas_height,
                             background='White', cursor="dot")
        self.canvas.pack(fill="both")
        self.canvas.bind("<B1-Motion>", self.paint)  # Bind mouse drag to drawing function
        self.canvas.bind("<ButtonRelease-1>", self.set_zero)  # Bind mouse release to set initial position to zero

        # Create main menu
        self.main_menu = Menu(self.root)
        self.root.config(menu=self.main_menu)

        # Create sub-menus
        self.create_color_menu()
        self.create_theme_menu()
        self.create_erase_menu()

    def create_color_menu(self):
        # Create color sub-menu
        self.color_menu = Menu(self.main_menu)
        self.main_menu.add_cascade(label="Colour", menu=self.color_menu)

        # Predefined colors as options
        colors = ["white", "blue", "red", "black"]
        for color in colors:
            self.color_menu.add_command(label="        ", background=color, command=lambda c=color: self.change_color(c))
        # Option to choose custom color
        self.color_menu.add_command(label="Other", command=self.change_fg)

    def create_theme_menu(self):
        # Create theme sub-menu
        self.theme_menu = Menu(self.main_menu)
        self.main_menu.add_cascade(label="Theme", menu=self.theme_menu)

        # Predefined themes
        self.theme_menu.add_command(label="       ", background="white", command=self.light_theme)
        
        # Option to choose custom background color
        

    def create_erase_menu(self):
        # Create erase sub-menu
        self.erase_menu = Menu(self.main_menu)
        self.main_menu.add_cascade(label="Erase", menu=self.erase_menu)
        # Option to clear the canvas
        self.erase_menu.add_command(label="Clear canvas", command=self.clear_canvas)
        self.erase_menu.add_checkbutton(label="Eraser", command=self.toggle_eraser)
    
    def toggle_eraser(self):
        # Toggle eraser mode and update drawing color accordingly
        self.eraser_mode = not self.eraser_mode
        if self.eraser_mode:
            self.colour = self.eraser_color
        else:
            self.colour = "black" 

    
    def change_color(self, color):
        self.colour = color

    def change_fg(self):
        # Ask user to choose a custom drawing color
        (triple, hexstr) = askcolor()
        if hexstr:
            self.colour = hexstr

    def change_bg(self):
        # Ask user to choose a custom background color for the canvas
        (triple, hexstr) = askcolor()
        if hexstr:
            self.canvas.config(background=hexstr)

    def light_theme(self):
        # Change the title and set canvas background to white for the light theme
        self.root.title("Rakib's Whiteboard")
        self.canvas.config(background="white")

    def dark_theme(self):
        # Change the title and set canvas background to black for the dark theme
        self.root.title("Rakib's blackboard")
        self.canvas.config(background="black")

    def paint(self, event):
        
        # Function to draw lines on the canvas while the mouse is dragged
        x1, y1 = event.x, event.y
        if self.x0 != 0 and self.y0 != 0:
            if self.eraser_mode:
                # Use eraser color when the eraser tool is active
                self.canvas.create_line(self.x0, self.y0, x1, y1, fill=self.eraser_color, width=self.s1.get(),
                                        capstyle=ROUND, smooth=True)
            else:
                # Use drawing color when the eraser tool is not active
                self.canvas.create_line(self.x0, self.y0, x1, y1, fill=self.colour, width=self.s1.get(),
                                        capstyle=ROUND, smooth=True)
        self.x0, self.y0 = x1, y1


    def set_zero(self, event):
        # Reset the initial position of the mouse cursor to zero when the mouse is released
        self.x0, self.y0 = 0, 0

    def clear_canvas(self):
        # Function to clear the entire canvas
        self.canvas.delete("all")


if __name__ == "__main__":
    root = Tk()
    app = WhiteboardApp(root)
    root.geometry(f"{app.canvas_width}x{app.canvas_height}")
    root.minsize(width=500, height=500)
    root.title("Rakib's board")
    root.mainloop()
