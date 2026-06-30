import tkinter as tk

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("OX Game - 2 Player")
        self.root.configure(bg="#1a1a1a") # Dark background modern look ke liye
        
        self.current_player = "X"
        self.board = [""] * 9
        self.buttons = []
        
        self.create_widgets()

    def create_widgets(self):
        # Heading Label
        self.label = tk.Label(self.root, text="Player X turn", font=('Helvetica', 16, 'bold'), bg="#1a1a1a", fg="#ffffff")
        self.label.pack(pady=15)
        
        # Grid ke liye ek frame
        frame = tk.Frame(self.root, bg="#1a1a1a")
        frame.pack()
        
        # 3x3 Grid ke Buttons banana
        for i in range(9):
            btn = tk.Button(
                frame, 
                text="", 
                font=('Helvetica', 24, 'bold'), 
                width=5, 
                height=2, 
                bg="#2d2d2d", 
                fg="#ffffff",
                activebackground="#3d3d3d",
                activeforeground="#ffffff",
                command=lambda idx=i: self.button_click(idx)
            )
            # Buttons ko 3 rows aur 3 columns mein set karna
            row = i // 3
            col = i % 3
            btn.grid(row=row, column=col, padx=5, pady=5)
            self.buttons.append(btn)

    def check_winner(self):
        # Jeetne ke saare patterns
        win_patterns = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8], # Horizontal
            [0, 3, 6], [1, 4, 7], [2, 5, 8], # Vertical
            [0, 4, 8], [2, 4, 6]             # Diagonal
        ]
        for pattern in win_patterns:
            if self.board[pattern[0]] == self.board[pattern[1]] == self.board[pattern[2]] != "":
                return pattern # Agar koi jeeta toh winning combination return karega
        return None

    def show_custom_congratulations(self, winner):
        """Ek dum mast balloons aur firework emojis waala custom popup window"""
        popup = tk.Toplevel(self.root)
        popup.title("🎉 WINNER! 🎉")
        popup.geometry("450x300")
        popup.configure(bg="#0f0f1a") # Fancy dark indigo theme
        popup.resizable(False, False)
        
        # Is pop-up ko main window ke upar lock karne ke liye
        popup.transient(self.root)
        popup.grab_set()

        # Balloons aur celebration decor labels
        balloons_left = tk.Label(popup, text="🎈\n🎈\n✨\n🎉", font=('Helvetica', 24), bg="#0f0f1a", fg="yellow")
        balloons_left.pack(side="left", padx=20)
        
        balloons_right = tk.Label(popup, text="🎈\n🎈\n✨\n🎉", font=('Helvetica', 24), bg="#0f0f1a", fg="yellow")
        balloons_right.pack(side="right", padx=20)

        # Beech ka badhai message content
        main_frame = tk.Frame(popup, bg="#0f0f1a")
        main_frame.pack(expand=True)

        congrats_lbl = tk.Label(main_frame, text="🎉 CONGRATULATIONS! 🎉", font=('Helvetica', 18, 'bold'), bg="#0f0f1a", fg="#ffcc00")
        congrats_lbl.pack(pady=10)

        winner_lbl = tk.Label(main_frame, text=f"PLAYER '{winner}'\nwinner!", font=('Helvetica', 16, 'bold'), bg="#0f0f1a", fg="#00ffcc")
        winner_lbl.pack(pady=10)

        decor_lbl = tk.Label(main_frame, text="🥳💥 🎈 💥🥳", font=('Helvetica', 16), bg="#0f0f1a")
        decor_lbl.pack(pady=5)

        # OK button jo game ko restart karega aur popup close karega
        ok_btn = tk.Button(
            main_frame, 
            text="NEXT GAME ➔", 
            font=('Helvetica', 12, 'bold'), 
            bg="#ff007f", 
            fg="white", 
            activebackground="#ff3399",
            activeforeground="white",
            padx=10, 
            pady=5, 
            bd=0,
            command=lambda: [popup.destroy(), self.reset_game()]
        )
        ok_btn.pack(pady=15)

    def button_click(self, idx):
        # Agar button khali hai toh hi click hoga
        if self.board[idx] == "":
            self.board[idx] = self.current_player
            
            # X ko Neon Blue aur O ko Neon Pink color dena (image "1000104122.jpg" ki tarah)
            if self.current_player == "X":
                self.buttons[idx].config(text="X", fg="#00d2ff", bg="#252525")
            else:
                self.buttons[idx].config(text="O", fg="#ff007f", bg="#252525")
            
            # Winner check karna
            winning_pattern = self.check_winner()
            if winning_pattern:
                # 1. Winning Line Effect: Jeetne waale teeno buttons ko Highlight karna
                for pos in winning_pattern:
                    self.buttons[pos].config(bg="#00ff66", fg="#1a1a1a", font=('Helvetica', 26, 'bold'))
                
                # Chhota sa delay taaki player pehle green line dekh sake, fir mast popup aaye
                self.root.after(600, lambda: self.show_custom_congratulations(self.current_player))
                return
                
            # Tie check karna
            if "" not in self.board:
                # Tie ke liye simple popup ya notification
                tie_popup = tk.Toplevel(self.root)
                tie_popup.title("Tie! 🤝")
                tie_popup.geometry("300x150")
                tie_popup.configure(bg="#1a1a1a")
                
                tk.Label(tie_popup, text="🤝 MATCH TIE! 🤝\n\nTIE TIE TIE", font=('Helvetica', 14, 'bold'), bg="#1a1a1a", fg="white").pack(pady=20)
                tk.Button(tie_popup, text="OK", font=('Helvetica', 10, 'bold'), width=10, bg="#2d2d2d", fg="white", command=lambda: [tie_popup.destroy(), self.reset_game()]).pack()
                return
            
            # Player badalna
            self.current_player = "O" if self.current_player == "X" else "X"
            self.label.config(text=f"Player {self.current_player} turn")

    def reset_game(self):
        # Board ko fir se saaf karna
        self.board = [""] * 9
        self.current_player = "X"
        self.label.config(text="Player X turn")
        for btn in self.buttons:
            btn.config(text="", bg="#2d2d2d", fg="#ffffff", font=('Helvetica', 24, 'bold'))

# Game chalane ke liye code
if __name__ == "__main__":
    root = tk.Tk()
    # Window ka size chota-bada na ho isliye fix kiya
    root.resizable(False, False) 
    game = TicTacToe(root)
    root.mainloop()