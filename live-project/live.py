import tkinter as tk
import random
from functools import partial
from tkinter import messagebox

# Emoji pairs
EMOJIS = ["🍎", "🍉", "🍇", "🥭", "🍍", "🥝"]

# Define colors for each emoji
EMOJI_COLORS = {
    "🍎": "red",
    "🍉": "green",
    "🍇": "purple",
    "🥭": "gold",
    "🍍": "orange",
    "🥝": "brown"
}

class MemoryGame:
    def __init__(self, root):
        self.root = root
        self.root.title("🌌 Memory Game")
        self.root.resizable(False, False)

        self.turns = 0
        self.buttons = []
        self.cards = []
        self.choice_one = None
        self.choice_two = None
        self.disabled = False

        self.setup_ui()
        self.shuffle_cards()

    def setup_ui(self):
        # Smaller canvas for small screen
        self.canvas = tk.Canvas(self.root, width=400, height=500, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        # Draw vertical gradient
        for i in range(500):
            r = 11
            g = 12
            b = 42 + i // 10
            color = f"#{r:02x}{g:02x}{b:02x}"
            self.canvas.create_line(0, i, 400, i, fill=color)

        # Title
        self.title_label = tk.Label(self.canvas, text="🌟 Memory Game 🌟",
                                    font=("Segoe UI Emoji", 20, "bold"),
                                    bg=None, fg="#FFD700")
        self.title_label.place(relx=0.5, y=20, anchor="center")

        # New Game button
        self.new_game_btn = tk.Button(self.canvas, text="🔄 New Game",
                                      command=self.shuffle_cards,
                                      bg="#1C1F4A", fg="#FFD700",
                                      font=("Arial", 10, "bold"),
                                      relief="raised", activebackground="#2C2F6C")
        self.new_game_btn.place(relx=0.5, y=60, anchor="center")

        # Grid frame
        self.grid_frame = tk.Frame(self.canvas, bg=None)
        self.grid_frame.place(relx=0.5, rely=0.55, anchor="center")

        # Turns label
        self.turns_label = tk.Label(self.canvas, text="Turns: 0",
                                    font=("Arial", 12, "bold"),
                                    bg=None, fg="#87CEEB")
        self.turns_label.place(relx=0.5, y=480, anchor="center")

    def shuffle_cards(self):
        self.cards = [{"emoji": e, "matched": False} for e in EMOJIS * 2]
        random.shuffle(self.cards)
        self.turns = 0
        self.choice_one = None
        self.choice_two = None
        self.disabled = False
        self.update_turns()
        self.render_grid()

    def render_grid(self):
        for widget in self.grid_frame.winfo_children():
            widget.destroy()
        self.buttons = []

        for index, card in enumerate(self.cards):
            btn = tk.Button(self.grid_frame, text="❓", width=6, height=3,
                            command=partial(self.handle_choice, index),
                            font=("Segoe UI Emoji", 18, "bold"), relief="raised",
                            bg="#1C1F4A", fg="white", activebackground="#2C2F6C")
            row = index // 4
            col = index % 4
            btn.grid(row=row, column=col, padx=3, pady=3)
            self.buttons.append(btn)

    def handle_choice(self, index):
        if self.disabled:
            return

        card = self.cards[index]
        btn = self.buttons[index]

        if card["matched"] or btn["text"] != "❓":
            return

        btn.config(text=card["emoji"], fg=EMOJI_COLORS.get(card["emoji"], "white"))

        if self.choice_one is None:
            self.choice_one = index
        elif self.choice_two is None:
            self.choice_two = index
            self.disabled = True
            self.root.after(800, self.check_match)

    def sparkle_effect(self, btn, emoji, color):
        btn.config(text=f"✨{emoji}✨", fg="gold")
        self.root.after(600, lambda: btn.config(text=emoji, fg=color))

    def check_match(self):
        c1 = self.cards[self.choice_one]
        c2 = self.cards[self.choice_two]

        if c1["emoji"] == c2["emoji"]:
            c1["matched"] = True
            c2["matched"] = True
            self.sparkle_effect(self.buttons[self.choice_one], c1["emoji"], EMOJI_COLORS[c1["emoji"]])
            self.sparkle_effect(self.buttons[self.choice_two], c2["emoji"], EMOJI_COLORS[c2["emoji"]])
        else:
            self.buttons[self.choice_one].config(text="❓", fg="white")
            self.buttons[self.choice_two].config(text="❓", fg="white")

        self.choice_one = None
        self.choice_two = None
        self.disabled = False
        self.turns += 1
        self.update_turns()

        if all(card["matched"] for card in self.cards):
            messagebox.showinfo("🌌 You Win! 🌟",
                                f"🎉 Congratulations! 🎉\nYou matched all pairs in {self.turns} turns!\n✨ Excellent memory under the stars! ✨")

    def update_turns(self):
        self.turns_label.config(text=f"Turns: {self.turns}")


if __name__ == "__main__":
    root = tk.Tk()
    game = MemoryGame(root)
    root.mainloop()