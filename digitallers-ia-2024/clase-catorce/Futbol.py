import tkinter as tk

class SoccerGame(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Juego de Futbol")
        self.geometry("800x600")
        self.resizable(False, False)

        self.main_menu()

    def main_menu(self):
        self.menu_frame = tk.Frame(self, bg="lightblue")
        self.menu_frame.pack(expand=True, fill="both")

        title_label = tk.Label(self.menu_frame, text="Juego de Futbol", font=("Helvetica", 30, "bold"), bg="lightblue")
        title_label.pack(pady=100)

        start_button = tk.Button(self.menu_frame, text="Empezar", font=("Helvetica", 20), command=self.start_game, bg="lightgreen", relief="groove", borderwidth=5)
        start_button.pack(pady=20)

        exit_button = tk.Button(self.menu_frame, text="Salir", font=("Helvetica", 20), command=self.quit, bg="lightcoral", relief="groove", borderwidth=5)
        exit_button.pack(pady=20)

    def start_game(self):
        self.menu_frame.pack_forget()
        self.canvas = tk.Canvas(self, width=800, height=600, bg="green")
        self.canvas.pack()

        # Draw field
        self.canvas.create_line(400, 0, 400, 600, fill="white")
        self.canvas.create_oval(350, 250, 450, 350, outline="white")
        self.canvas.create_rectangle(0, 200, 50, 400, outline="white")
        self.canvas.create_rectangle(750, 200, 800, 400, outline="white")

        # Create players
        self.player_red = self.canvas.create_rectangle(100, 300, 120, 320, fill="red")
        self.player_blue = self.canvas.create_rectangle(680, 300, 700, 320, fill="blue")

        # Create ball
        self.ball = self.canvas.create_oval(390, 290, 410, 310, fill="white")

        # Score
        self.score_red = 0
        self.score_blue = 0
        self.score_display = self.canvas.create_text(400, 30, text="Rojo: 0  Azul: 0", font=("Helvetica", 20), fill="white")

        # Speeds
        self.ball_dx = 0
        self.ball_dy = 0

        # Controls
        self.bind("<KeyPress>", self.key_press)
        self.bind("<KeyRelease>", self.key_release)

        self.red_movement = {"x": 0, "y": 0}
        self.blue_movement = {"x": 0, "y": 0}

        self.after(20, self.update_game)

    def key_press(self, event):
        if event.char == "w":
            self.red_movement["y"] = -5
        elif event.char == "s":
            self.red_movement["y"] = 5
        elif event.char == "a":
            self.red_movement["x"] = -5
        elif event.char == "d":
            self.red_movement["x"] = 5
        elif event.char == "i":
            self.blue_movement["y"] = -5
        elif event.char == "k":
            self.blue_movement["y"] = 5
        elif event.char == "j":
            self.blue_movement["x"] = -5
        elif event.char == "l":
            self.blue_movement["x"] = 5
        elif event.char == "r":
            self.restart_game()

    def key_release(self, event):
        if event.char in ("w", "s"):
            self.red_movement["y"] = 0
        elif event.char in ("a", "d"):
            self.red_movement["x"] = 0
        elif event.char in ("i", "k"):
            self.blue_movement["y"] = 0
        elif event.char in ("j", "l"):
            self.blue_movement["x"] = 0

    def update_game(self):
        # Move players
        self.move_player(self.player_red, self.red_movement)
        self.move_player(self.player_blue, self.blue_movement)

        # Move ball
        ball_coords = self.canvas.coords(self.ball)
        if self.is_near(self.player_red, ball_coords):
            self.ball_dx, self.ball_dy = self.red_movement["x"], self.red_movement["y"]
        elif self.is_near(self.player_blue, ball_coords):
            self.ball_dx, self.ball_dy = self.blue_movement["x"], self.blue_movement["y"]
        else:
            self.ball_dx, self.ball_dy = 0, 0

        self.canvas.move(self.ball, self.ball_dx, self.ball_dy)

        # Check boundaries
        self.check_boundaries(self.player_red)
        self.check_boundaries(self.player_blue)
        self.check_ball_boundaries()

        # Update score and check for goals
        if ball_coords[0] <= 0:
            self.score_blue += 1
            self.reset_positions()
        elif ball_coords[2] >= 800:
            self.score_red += 1
            self.reset_positions()

        self.canvas.itemconfig(self.score_display, text=f"Rojo: {self.score_red}  Azul: {self.score_blue}")

        # Check for a winner
        if self.score_red >= 5:
            self.display_winner("¡Rojo")
        elif self.score_blue >= 5:
            self.display_winner("¡Azul")
        else:
            self.after(20, self.update_game)

    def move_player(self, player, movement):
        self.canvas.move(player, movement["x"], movement["y"])

    def is_near(self, player, ball_coords):
        player_coords = self.canvas.coords(player)
        return (
            player_coords[0] < ball_coords[2] and
            player_coords[2] > ball_coords[0] and
            player_coords[1] < ball_coords[3] and
            player_coords[3] > ball_coords[1]
        )

    def check_boundaries(self, player):
        coords = self.canvas.coords(player)
        if coords[0] < 0:
            self.canvas.move(player, -coords[0], 0)
        elif coords[2] > 800:
            self.canvas.move(player, 800 - coords[2], 0)
        if coords[1] < 0:
            self.canvas.move(player, 0, -coords[1])
        elif coords[3] > 600:
            self.canvas.move(player, 0, 600 - coords[3])

    def check_ball_boundaries(self):
        coords = self.canvas.coords(self.ball)
        if coords[0] < 0 or coords[2] > 800:
            self.ball_dx = 0
        if coords[1] < 0 or coords[3] > 600:
            self.ball_dy = 0

    def reset_positions(self):
        self.canvas.coords(self.player_red, 100, 300, 120, 320)
        self.canvas.coords(self.player_blue, 680, 300, 700, 320)
        self.canvas.coords(self.ball, 390, 290, 410, 310)

    def display_winner(self, winner):
        self.canvas.create_text(400, 300, text=f"{winner} Gana!\nPresiona 'R'", font=("Helvetica", 40), fill="yellow")
        self.unbind("<KeyPress>")
        self.unbind("<KeyRelease>")
        self.bind("<KeyPress-r>", self.restart_game)

    def restart_game(self, event=None):
        self.canvas.pack_forget()
        self.start_game()

if __name__ == "__main__":
    game = SoccerGame()
    game.mainloop()
