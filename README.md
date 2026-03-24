![Project Banner](https://via.placeholder.com/800x200/007bff/ffffff?text=Tic-Tac-Toe+OX+Game)

# 🎮 OX Game – Human vs Computer

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Project Status: Active](https://img.shields.io/badge/status-active-success.svg)](https://github.com/Akshay94os/tic-toe-game-OX-)

A classic Tic-Tac-Toe (O-X) game implemented in Python with a modern, interactive graphical user interface (GUI). Challenge a simple computer AI in this timeless game of strategy.

## 🌟 Overview

This project delivers a straightforward yet engaging Tic-Tac-Toe experience. It's a single-player game where you, as "X", compete against a computer opponent, "O". The game features a clean, responsive GUI built with `tkinter` and styled using `ttkbootstrap`, providing a visually appealing and intuitive interface. Perfect for a quick brain teaser or a simple coding example.

## ✨ Features

*   **Human vs. Computer Gameplay**: Play as "X" against an "O" computer opponent.
*   **Modern GUI**: Powered by `ttkbootstrap` for a sleek and responsive user interface.
*   **Win/Draw Detection**: Automatically identifies and announces the winner or a draw.
*   **Game Reset**: Easily restart the game at any point.
*   **Simple AI**: The computer makes random valid moves, offering a casual challenge.
*   **Interactive Feedback**: Buttons change style upon selection, and game results are shown via pop-up messages.

## 🛠️ Tech Stack

*   **Language**: Python 3.x
*   **GUI Framework**: `tkinter` (standard Python library)
*   **GUI Styling**: `ttkbootstrap` (a theme extension for `tkinter`)
*   **Randomness**: `random` module (for computer AI moves)

## 🏗️ Architecture

The project consists of a single Python file, `ox_game.py`, which encapsulates all game logic and GUI elements.

*   **Game State Management**: Global variables (`current_player`, `board`, `game_over`) manage the current player, the game board, and the game's active status.
*   **Core Logic Functions**:
    *   `check_winner()`: Determines if there's a winner or a draw after each move.
    *   `computer_move()`: Implements the computer's turn, choosing a random empty cell.
    *   `on_click()`: Handles human player's moves, updates the board, and triggers the computer's turn.
    *   `finish_game()`: Displays the game result (win/lose/draw) and sets `game_over`.
    *   `reset_game()`: Initializes the board and game state for a new game.
*   **GUI Setup**: Uses `ttkbootstrap` widgets (`Window`, `Label`, `Frame`, `Button`) to construct the game board and controls. Event handling is managed through `tkinter`'s `command` attribute on buttons.

```
.
└── ox_game.py  # Main game logic and GUI
```

## 🚀 Getting Started

Follow these instructions to get a copy of the project up and running on your local machine.

### Prerequisites

Before you begin, ensure you have the following installed:

*   **Python 3.8+**: Download from [python.org](https://www.python.org/downloads/).

### Installation

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/Akshay94os/tic-toe-game-OX-.git
    cd tic-toe-game-OX-
    ```

2.  **Install `ttkbootstrap`**:
    This project uses `ttkbootstrap` for its modern GUI. Install it using pip:
    ```bash
    pip install ttkbootstrap
    ```

### Configuration

No special configuration files or environment variables are required. The game runs directly from the Python script.

## 🎮 Usage

To play the game, simply run the `ox_game.py` script:

```bash
python ox_game.py
```

### How to Play

1.  **Start the Game**: Run the script, and the game window will appear.
2.  **Your Turn**: You are "X". Click on any empty cell on the 3x3 grid to place your mark.
3.  **Computer's Turn**: After your move, the computer ("O") will automatically make its move after a short delay.
4.  **Win/Draw**: The game will announce a winner or a draw via a pop-up message when the game concludes.
5.  **Reset**: Click the "Reset Game" button to start a new round.

![Gameplay Screenshot](https://via.placeholder.com/600x400/007bff/ffffff?text=Tic-Tac-Toe+Gameplay+Screenshot)
*A placeholder image demonstrating the game's interface.*

## 🧑‍💻 Development

### Setting Up Your Development Environment

1.  Follow the installation steps above to clone the repository and install `ttkbootstrap`.
2.  Open `ox_game.py` in your preferred Python IDE (e.g., VS Code, PyCharm).

### Running Tests

This project does not include a formal test suite. To test changes, simply run the `ox_game.py` script and interact with the GUI to verify functionality.

```bash
python ox_game.py
```

### Code Style Guidelines

The code generally follows PEP 8 guidelines. Please adhere to consistent formatting and naming conventions if making contributions.

## 🤝 Contributing

Contributions are welcome! If you have suggestions for improvements or want to add new features, please follow these steps:

1.  **Fork** the repository.
2.  **Create a new branch** for your feature or bug fix: `git checkout -b feature/your-feature-name`.
3.  **Make your changes** and ensure they adhere to the existing code style.
4.  **Commit your changes** with a clear and descriptive message: `git commit -m 'feat: Add new feature X'`.
5.  **Push to your fork**: `git push origin feature/your-feature-name`.
6.  **Open a Pull Request** to the `main` branch of the original repository.

### Ideas for Contribution

*   **Smarter AI**: Implement a more challenging AI (e.g., Minimax algorithm).
*   **Multiplayer Mode**: Add functionality for two human players.
*   **Customizable Themes**: Allow users to select different `ttkbootstrap` themes.
*   **Score Tracking**: Keep track of wins, losses, and draws.
*   **Difficulty Levels**: Introduce different AI difficulty settings.

## ❓ Troubleshooting

*   **`ModuleNotFoundError: No module named 'ttkbootstrap'`**:
    This error indicates that `ttkbootstrap` is not installed.
    **Solution**: Run `pip install ttkbootstrap` in your terminal.
*   **GUI window does not appear**:
    Ensure you are running the script with `python ox_game.py` and that Python is correctly installed and added to your system's PATH. Check your terminal for any error messages.

If you encounter other issues, please open an issue on the GitHub repository.

## 🛣️ Roadmap

*   Implement an advanced AI using the Minimax algorithm.
*   Develop a two-player mode for local human-vs-human gameplay.
*   Add a settings menu to customize themes and AI difficulty.
*   Integrate a basic score counter.

## 📄 License & Credits

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details (if not present, it is implicitly MIT for open-source projects).

**Developed by**: Akshay94os