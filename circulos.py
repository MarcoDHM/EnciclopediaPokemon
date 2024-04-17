import tkinter as tk
import random

class Balloon:
    def __init__(self, canvas, game):
        self.canvas = canvas
        self.size = random.randint(20, 50)
        self.color = self.random_color()
        self.game = game
        self.click_count = 0  # Contador de clics para cada globo
        self.id = canvas.create_oval(0, 0, self.size, self.size, fill=self.color, outline=self.color)
        self.canvas.move(self.id, random.uniform(0, 750 - self.size), random.uniform(0, 550 - self.size))
        self.speed_x = random.uniform(-2, 2)
        self.speed_y = random.uniform(-2, 2)

    def random_color(self):
        colors = ["red", "blue", "green", "yellow", "purple", "orange"]
        return random.choice(colors)

    def move(self):
        self.canvas.move(self.id, self.speed_x, self.speed_y)
        pos = self.canvas.coords(self.id)

        if pos[0] <= 0 or pos[2] >= 800:  # Ajusta los límites para el nuevo tamaño del lienzo
            self.speed_x = -self.speed_x
        if pos[1] <= 0 or pos[3] >= 600:  # Ajusta los límites para el nuevo tamaño del lienzo
            self.speed_y = -self.speed_y

    def pop(self):
        self.click_count += 1
        self.canvas.delete(self.id)
        self.game.increment_counter()
        self.game.create_balloon()

class BalloonGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Balloon Game")
        self.root.geometry("800x600")
        self.root.configure(bg="black")

        self.canvas = tk.Canvas(root, bg="black", width=800, height=600)
        self.canvas.pack()

        self.balloons = []
        self.counter = 0
        self.counter_label = tk.Label(root, text="Globos Explotados: 0", fg="white", bg="black", font=("Helvetica", 20))
        self.counter_label.pack()

        self.create_balloons()
        self.animate()

    def create_balloons(self):
        for _ in range(20):
            balloon = Balloon(self.canvas, self)
            self.balloons.append(balloon)

    def animate(self):
        for balloon in self.balloons:
            balloon.move()

        self.root.after(20, self.animate)

    def pop_balloon(self, event):
        x, y = event.x, event.y
        popped_balloons = []
        for balloon in self.balloons:
            pos = self.canvas.coords(balloon.id)
            if pos[0] <= x <= pos[2] and pos[1] <= y <= pos[3]:
                balloon.pop()
                popped_balloons.append(balloon)
        for popped_balloon in popped_balloons:
            self.balloons.remove(popped_balloon)

    def increment_counter(self):
        self.counter += 1
        self.update_counter()

    def update_counter(self):
        self.counter_label.config(text=f"Globos Explotados: {self.counter}")

    def create_balloon(self):
        balloon = Balloon(self.canvas, self)
        self.balloons.append(balloon)

if __name__ == "__main__":
    root = tk.Tk()
    game = BalloonGame(root)
    root.bind("<Button-1>", game.pop_balloon)
    root.mainloop()
