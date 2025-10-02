## 📌 MEMORY GAME

A simple, interactive **Memory Game** developed as a desktop application to help improve concentration and short-term memory skills. The project is built entirely using **Python** with the **Tkinter** library for the graphical user interface.

## 📑 Table of Contents
- [📌 About the Project](#-about-the-project)
- [✨ Key Features](#-key-features)
- [⚙️ How It Works](#️-how-it-works)
- [🚀 Getting Started](#-getting-started)
- [📂 Project Structure](#-project-structure)
- [🖥️ Screenshots](#️-screenshots)
- [🔮 Future Enhancements](#-future-enhancements)

---

## 📌 About the Project

[cite_start]This system is an **interactive puzzle game** designed for both entertainment and educational purposes[cite: 27, 37]. [cite_start]It is a lightweight, user-friendly application suitable for all age groups[cite: 41].

The main objectives of this project were to:
1.  [cite_start]Design and develop an interactive memory game using Python[cite: 46].
2.  [cite_start]Demonstrate the use of **Tkinter** for GUI-based applications[cite: 47].
3.  [cite_start]Implement basic game logic like card shuffling and turn counting[cite: 48].

---

## ✨ Key Features
-   [cite_start]**Interactive GUI:** Built with **Python's Tkinter** library[cite: 26, 39].
-   [cite_start]**Core Gameplay:** Players flip cards to reveal **emojis** and try to match pairs[cite: 28, 40].
-   [cite_start]**Turn Counting:** The system records and displays the number of turns taken[cite: 29].
-   [cite_start]**Visual Feedback:** A **sparkle effect** is shown when a match is successfully found[cite: 155, 159].
-   [cite_start]**Game Completion:** A congratulatory pop-up message is displayed upon matching all pairs[cite: 29, 146, 156].
-   [cite_start]**Game Controls:** Includes a **"New Game"** button to quickly reshuffle and restart[cite: 103, 104, 106].

---

## ⚙️ How It Works

The game follows a simple logic flow:

1.  [cite_start]**Setup:** The game initializes the canvas with a background gradient, a title, and a "New Game" button[cite: 101, 104, 153].
2.  [cite_start]**Shuffling:** An array of emoji pairs is created, and the cards are **randomly shuffled**[cite: 125, 126, 154].
3.  [cite_start]**User Choice:** When the user clicks a button, the corresponding hidden emoji is revealed[cite: 141, 158].
4.  [cite_start]**Matching Logic:** After two cards are flipped, the system checks if the two emojis match[cite: 142].
    * [cite_start]If they **match**, they stay revealed, and a sparkle effect is applied[cite: 143, 144].
    * [cite_start]If they **don't match**, the cards flip back to the hidden `❓` symbol after a short delay[cite: 145].
5.  [cite_start]**Turn Update:** The turn counter is incremented after every pair of choices[cite: 145].
6.  **Win Condition:** The game checks if all card pairs have been matched. [cite_start]If so, it shows the winning message[cite: 145, 146].

---

## 🚀 Getting Started

To run this project locally, you only need a working Python environment.

### Prerequisites

* **Python 3.x**
* The required libraries (`tkinter`, `random`, `functools`, `messagebox`) are all standard or built-in with Python.

### Running the Game

1.  Navigate to the project directory in your terminal.
2.  Run the main Python file:

```bash
python <your-main-file>.py