import tkinter as tk

class DragDropGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Drag and Drop Game")

        self.circles = []
        self.rectangles = []

        colors = ["#e74c3c", "#2ecc71", "#3498db"]  # Red, Green, Blue

        for i in range(3):
            circle = tk.Canvas(root, bg=colors[i], width=30, height=30)
            circle.create_oval(5, 5, 25, 25, fill="white", outline="black")
            circle.place(x=50 + i * 150, y=150)
            self.circles.append(circle)

            rectangle = tk.Canvas(root, bg=colors[i], width=50, height=50)
            rectangle.create_rectangle(5, 5, 45, 45, fill="white", outline="black")
            rectangle.place(x=25 + i * 150, y=350)
            self.rectangles.append(rectangle)

            circle.bind("<ButtonPress-1>", lambda event, index=i: self.on_drag_start(event, index))
            circle.bind("<B1-Motion>", self.on_drag_motion)
            circle.bind("<ButtonRelease-1>", lambda event, index=i: self.on_drag_release(event, index))

        self.win_label = tk.Label(root, text="You win!", fg="green", font=("Helvetica", 16))

    def on_drag_start(self, event, index):
        self.dragged_circle = self.circles[index]
        self.start_x = event.x
        self.start_y = event.y

    def on_drag_motion(self, event):
        if hasattr(self, 'dragged_circle'):
            x = self.dragged_circle.winfo_x() - self.start_x + event.x
            y = self.dragged_circle.winfo_y() - self.start_y + event.y
            self.dragged_circle.place(x=x, y=y)

    def on_drag_release(self, event, index):
        if hasattr(self, 'dragged_circle'):
            circle_x, circle_y = self.dragged_circle.winfo_x(), self.dragged_circle.winfo_y()

            for i, rectangle in enumerate(self.rectangles):
                rectangle_x, rectangle_y = rectangle.winfo_x(), rectangle.winfo_y()

                if (
                    rectangle_x <= circle_x <= rectangle_x + rectangle.winfo_reqwidth() and
                    rectangle_y <= circle_y <= rectangle_y + rectangle.winfo_reqheight()
                ):
                    self.dragged_circle.place(in_=rectangle, x=10, y=10)
                    break
            else:
                self.dragged_circle.place(x=self.start_x, y=self.start_y)

            # Check for a win
            if all(self.dragged_circle.winfo_parent() == rectangle for self.dragged_circle, rectangle in zip(self.circles, self.rectangles)):
                self.win_label.pack()

            del self.dragged_circle

if __name__ == "__main__":
    root = tk.Tk()
    game = DragDropGame(root)
    root.geometry("600x500")
    root.mainloop()
