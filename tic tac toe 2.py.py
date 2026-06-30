import tkinter as tk

class TicTacToeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe - Neon Glow")
        self.root.geometry("400x650")
        self.root.configure(bg="#0b0b1e")  # Dark Neon Background
        self.root.resizable(False, False)

        self.game_mode = "PvP"  # Default mode
        self.current_player = "O"  # Player 1 is O, Player 2 is X
        self.board = [""] * 9
        self.buttons = []
        self.game_active = True

        # Sabse pehle Menu Screen load hogi
        self.show_menu_screen()

    def clear_screen(self):
        """Purane saare widgets ko screen se hatane ke liye"""
        for widget in self.root.winfo_children():
            widget.destroy()

    # ==================== 1. MENU SCREEN ====================
    def show_menu_screen(self):
        self.clear_screen()

        # Title
        title_lbl = tk.Label(self.root, text="SELECT LEVEL", font=('Helvetica', 22, 'bold'), bg="#0b0b1e", fg="#ffffff")
        title_lbl.pack(pady=40)

        # Game Icon Preview (Dummy Neon Box)
        preview_frame = tk.Frame(self.root, bg="#0b0b1e", highlightbackground="#00ffff", highlightthickness=3, bd=0)
        preview_frame.pack(pady=10)
        preview_lbl = tk.Label(preview_frame, text=" O │ X │   \n───┼───┼───\n   │ O │ X \n───┼───┼───\n X │   │ O ", 
                               font=('Courier', 20, 'bold'), bg="#0b0b1e", fg="#ff007f", padx=20, pady=20)
        preview_lbl.pack()

        # Dots Indicator
        dots_lbl = tk.Label(self.root, text="●  ○  ○  ○", font=('Helvetica', 14), bg="#0b0b1e", fg="#ffffff")
        dots_lbl.pack(pady=15)

        # Buttons Frame
        btn_frame = tk.Frame(self.root, bg="#0b0b1e")
        btn_frame.pack(pady=20)

        # Mode Buttons
        vs_comp_btn = tk.Button(btn_frame, text="👤  vs  💻", font=('Helvetica', 16, 'bold'), bg="#0b0b1e", fg="#00ffff",
                                activebackground="#00ffff", activeforeground="#0b0b1e", width=18, bd=2, relief="solid",
                                command=lambda: self.start_game("PvC"))
        vs_comp_btn.grid(row=0, column=0, pady=10)

        vs_player_btn = tk.Button(btn_frame, text="👤  vs  👤", font=('Helvetica', 16, 'bold'), bg="#0b0b1e", fg="#ffcc00",
                                  activebackground="#ffcc00", activeforeground="#0b0b1e", width=18, bd=2, relief="solid",
                                  command=lambda: self.start_game("PvP"))
        vs_player_btn.grid(row=1, column=0, pady=10)

        campaign_btn = tk.Button(btn_frame, text="CAMPAIGN", font=('Helvetica', 16, 'bold'), bg="#0b0b1e", fg="#ff5500",
                                 activebackground="#ff5500", activeforeground="#0b0b1e", width=18, bd=2, relief="solid",
                                 command=lambda: self.start_game("PvP"))
        campaign_btn.grid(row=2, column=0, pady=10)

    def start_game(self, mode):
        self.game_mode = mode
        self.board = [""] * 9
        self.current_player = "O"  # Player 1 = O
        self.game_active = True
        self.show_game_screen()

    # ==================== 2. GAME PLAY SCREEN ====================
    def show_game_screen(self):
        self.clear_screen()

        # Top Status Scorebar
        status_frame = tk.Frame(self.root, bg="#0b0b1e")
        status_frame.pack(pady=20)

        self.p1_lbl = tk.Label(status_frame, text="⭕\nPLAYER 1", font=('Helvetica', 12, 'bold'), bg="#0b0b1e", fg="#00ffff")
        self.p1_lbl.grid(row=0, column=0, padx=40)

        vs_lbl = tk.Label(status_frame, text="VS", font=('Helvetica', 16, 'bold'), bg="#0b0b1e", fg="#ffffff")
        vs_lbl.grid(row=0, column=1)

        self.p2_lbl = tk.Label(status_frame, text="❌\nPLAYER 2", font=('Helvetica', 12, 'bold'), bg="#0b0b1e", fg="#ff007f")
        self.p2_lbl.grid(row=0, column=2, padx=40)

        # Board Container (Canvas is used to draw the winning line)
        self.canvas = tk.Canvas(self.root, width=320, height=320, bg="#0b0b1e", highlightthickness=3, highlightbackground="#00ffff")
        self.canvas.pack(pady=20)

        # Canvas ke andar 3x3 Grid Ke Buttons fit karna
        self.buttons = []
        for i in range(9):
            row = i // 3
            col = i % 3
            # Har button ka x, y coordinates canvas ke mutabik calculate kiya
            x = col * 105 + 10
            y = row * 105 + 10
            
            btn = tk.Button(self.canvas, text="", font=('Helvetica', 28, 'bold'), bg="#11112a", fg="#ffffff",
                            activebackground="#1a1a3a", bd=0, width=4, height=2,
                            command=lambda idx=i: self.cell_clicked(idx))
            
            # Button ko canvas ke upar attach karna
            self.canvas.create_window(x, y, anchor="nw", window=btn, width=95, height=95)
            self.buttons.append(btn)

    def cell_clicked(self, idx):
        if self.board[idx] == "" and self.game_active:
            self.board[idx] = self.current_player
            
            # Neon Styles jaisa color allocation
            if self.current_player == "O":
                self.buttons[idx].config(text="O", fg="#00ffff")  # Neon Blue
                winning_color = "#00ffff"
            else:
                self.buttons[idx].config(text="X", fg="#ff007f")  # Neon Pink
                winning_color = "#ff007f"

            # Check Winner
            win_pattern = self.check_winner()
            if win_pattern:
                self.game_active = False
                self.draw_winning_line(win_pattern, winning_color)
                # 0.5 second baad Overlay (Win Screen) aayega taaki player line dekh sake
                self.root.after(500, lambda: self.show_win_overlay(f"PLAYER {'1' if self.current_player == 'O' else '2'} WIN"))
                return

            if "" not in self.board:
                self.game_active = False
                self.show_win_overlay("MATCH TIE")
                return

            # Player Switch
            self.current_player = "X" if self.current_player == "O" else "O"

    def check_winner(self):
        win_patterns = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8], # Horizontal
            [0, 3, 6], [1, 4, 7], [2, 5, 8], # Vertical
            [0, 4, 8], [2, 4, 6]             # Diagonal
        ]
        for pattern in win_patterns:
            if self.board[pattern[0]] == self.board[pattern[1]] == self.board[pattern[2]] != "":
                return pattern
        return None

    def draw_winning_line(self, pattern, color):
        """Buttons ke upar se asli glowing line draw karne ke liye"""
        # Centers of grid cells
        coords = {
            0: (57, 57),   1: (162, 57),  2: (267, 57),
            3: (57, 162),  4: (162, 162), 5: (267, 162),
            6: (57, 267),  7: (162, 267), 8: (267, 267)
        }
        x1, y1 = coords[pattern[0]]
        x2, y2 = coords[pattern[2]]
        
        # Canvas par line draw karna jo buttons ke beech se niklegi (bilkul Screenshot 2 ki tarah)
        self.canvas.create_line(x1, y1, x2, y2, fill=color, width=8, capstyle="round")

    # ==================== 3. WINNER OVERLAY (SCREEN 3) ====================
    def show_win_overlay(self, message):
        """Popup nahi, screen ke upar hi confetti aur buttons dikhane ke liye"""
        # Purane layout ko lock karke center mein winner box overlay banana
        self.overlay_frame = tk.Frame(self.root, bg="#0b0b1e", highlightbackground="#ffcc00", highlightthickness=3)
        self.overlay_frame.place(relx=0.5, rely=0.5, anchor="center", width=340, height=340)

        # Celebration Emojis (Confetti decoration)
        confetti_lbl = tk.Label(self.overlay_frame, text="🎉  ✨  👑  ✨  🎉\n✨   🎈   🎈   ✨", 
                                font=('Helvetica', 14), bg="#0b0b1e", fg="#ffcc00")
        confetti_lbl.pack(pady=15)

        # "PLAYER 1 WIN" Banner text
        win_text_lbl = tk.Label(self.overlay_frame, text=message, font=('Helvetica', 24, 'bold'), bg="#0b0b1e", fg="#ffcc00")
        win_text_lbl.pack(pady=10)

        # HOME BUTTON
        home_btn = tk.Button(self.overlay_frame, text="🏠   HOME", font=('Helvetica', 14, 'bold'), bg="#00ffff", fg="#0b0b1e",
                             activebackground="#00cccc", width=15, bd=0, pady=8, command=self.show_menu_screen)
        home_btn.pack(pady=10)

        # REPLAY BUTTON
        replay_btn = tk.Button(self.overlay_frame, text="🔄   REPLAY", font=('Helvetica', 14, 'bold'), bg="#ff5500", fg="#ffffff",
                               activebackground="#dd4400", width=15, bd=0, pady=8, command=lambda: self.start_game(self.game_mode))
        replay_btn.pack(pady=10)

# App run karne ke liye loop
if __name__ == "__main__":
    root = tk.Tk()
    app = TicTacToeApp(root)
    root.mainloop()