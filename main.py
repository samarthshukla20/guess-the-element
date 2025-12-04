import tkinter as tk
from tkinter import messagebox, font
import random

try:
    from mendeleev import get_all_elements
    print("Loading Chemical Database...")
    ELEMENTS = get_all_elements()

    ELEMENTS = [e for e in ELEMENTS if e.atomic_number <= 118]
except ImportError:
    print("Mendeleev library not found. Using fallback mode.")

    class MockElement:
        def __init__(self, an, name, sym, grp, per, blk, ser, conf, mass, n):
            self.atomic_number = an
            self.name = name
            self.symbol = sym
            self.group_id = grp
            self.period = per
            self.block = blk
            self.series = ser
            self.econf = conf
            self.mass = mass
            self.neutrons = n

    ELEMENTS = [
        MockElement(1, "Hydrogen", "H", 1, 1, "s", "Nonmetal", "1s1", 1.008, 0),
        MockElement(2, "Helium", "He", 18, 1, "s", "Noble Gas", "1s2", 4.0026, 2),
        MockElement(6, "Carbon", "C", 14, 2, "p", "Nonmetal", "[He] 2s2 2p2", 12.011, 6),
        MockElement(8, "Oxygen", "O", 16, 2, "p", "Nonmetal", "[He] 2s2 2p4", 15.999, 8),
        MockElement(26, "Iron", "Fe", 8, 4, "d", "Transition Metal", "[Ar] 3d6 4s2", 55.845, 30),
        MockElement(79, "Gold", "Au", 11, 6, "d", "Transition Metal", "[Xe] 4f14 5d10 6s1", 196.97, 118),
    ]

class ElementGameGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Computational Chemistry: Element Guess")
        self.root.geometry("600x750")
        
        self.bg_color = "#121212"    
        self.card_bg = "#1e1e24"        
        self.text_color = "#ffffff"     
        self.accent_color = "#00f3ff"   
        self.success_color = "#00ff41"  
        self.error_color = "#ff0055"    
        self.secondary_text = "#a0a0a0" 

        self.root.configure(bg=self.bg_color)
        
        self.header_font = font.Font(family="Helvetica", size=20, weight="bold")
        self.normal_font = font.Font(family="Consolas", size=11)
        self.bold_font = font.Font(family="Consolas", size=11, weight="bold")
        
        self.target = None
        self.attempts = 0
        self.max_attempts = 6
        self.game_over = False

        self.create_widgets()
        self.start_new_game()

    def create_widgets(self):
        header_frame = tk.Frame(self.root, bg=self.bg_color, pady=20)
        header_frame.pack(fill="x")
        
        tk.Label(header_frame, text="GUESS THE ELEMENT", font=self.header_font, 
                 bg=self.bg_color, fg=self.accent_color).pack()
        tk.Label(header_frame, text="Computational Chemistry Project (by Group-2)", 
                 font=("Helvetica", 10), bg=self.bg_color, fg=self.secondary_text).pack()

        self.status_label = tk.Label(self.root, text="Attempts: 0/6", font=self.bold_font,
                                     bg=self.bg_color, fg=self.text_color)
        self.status_label.pack(pady=5)

        input_frame = tk.Frame(self.root, bg=self.card_bg, padx=20, pady=20, relief="flat", bd=0)
        input_frame.pack(fill="x", padx=20, pady=10)

        tk.Label(input_frame, text="Enter Element Name or Symbol:", 
                 font=self.normal_font, bg=self.card_bg, fg=self.text_color).pack(anchor="w")
        
        self.entry = tk.Entry(input_frame, font=("Helvetica", 14), bg="#2b2b36", 
                              fg=self.text_color, insertbackground="white", relief="flat")
        self.entry.pack(fill="x", pady=10)
        self.entry.bind("<Return>", self.check_guess)

        btn_frame = tk.Frame(input_frame, bg=self.card_bg)
        btn_frame.pack(fill="x")

        self.guess_btn = tk.Button(btn_frame, text="ANALYZE", font=self.bold_font, 
                                   bg=self.accent_color, fg="#000000", activebackground="#00dbe6",
                                   relief="flat", command=self.check_guess, cursor="hand2")
        self.guess_btn.pack(side="left", expand=True, fill="x", padx=(0, 5))

        self.reset_btn = tk.Button(btn_frame, text="RESET", font=self.bold_font,
                                   bg="#333333", fg="white", activebackground="#444444",
                                   relief="flat", command=self.start_new_game, cursor="hand2")
        self.reset_btn.pack(side="right", padx=(5, 0))

        self.feedback_frame = tk.Frame(self.root, bg=self.bg_color)
        self.feedback_frame.pack(fill="both", expand=True, padx=20, pady=10)

        self.hint_label = tk.Label(self.feedback_frame, text="Hint: Game Started", 
                                   font=self.normal_font, bg=self.bg_color, fg=self.secondary_text, wraplength=550)
        self.hint_label.pack(pady=(0, 10))

        self.history_text = tk.Text(self.feedback_frame, bg=self.card_bg, fg=self.text_color,
                                    font=self.normal_font, state="disabled", height=15,
                                    relief="flat", padx=10, pady=10)
        self.history_text.pack(fill="both", expand=True)
        
        self.history_text.tag_config("success", foreground=self.success_color)
        self.history_text.tag_config("warning", foreground="#ffd700")
        self.history_text.tag_config("info", foreground=self.accent_color)
        self.history_text.tag_config("error", foreground=self.error_color)

    def start_new_game(self):
        self.target = random.choice(ELEMENTS)
        self.attempts = 0
        self.game_over = False
        
        self.update_status()
        self.entry.delete(0, tk.END)
        self.entry.config(state="normal")
        self.guess_btn.config(state="normal", bg=self.accent_color)
        self.hint_label.config(text="System Ready. Enter your first guess.", fg=self.secondary_text)
        
        self.history_text.config(state="normal")
        self.history_text.delete(1.0, tk.END)
        self.history_text.insert(tk.END, f"TARGET LOCKED. Range: 1-118\n{'-'*40}\n")
        self.history_text.config(state="disabled")
        
        print(f"DEBUG: Target is {self.target.name}")

    def update_status(self):
        self.status_label.config(text=f"Attempts: {self.attempts}/{self.max_attempts}")

    def get_hint(self):
   
        if self.attempts == 0: return "Guess to unlock hints."
        if self.attempts == 1: return f"Hint: This element belongs to the {self.target.block}-block."
        if self.attempts == 2: return f"Hint: It is a {self.target.series}."
        if self.attempts == 3: 

            last_orbital = self.target.econf.split()[-1] if hasattr(self.target, 'econf') else "Unknown"
            return f"Hint: Electron config ends in {last_orbital}."
        if self.attempts == 4: return f"Hint: Approx Atomic Mass is {self.target.mass:.1f}."
        return "Hint: Think about the Atomic Number!"

    def check_guess(self, event=None):
        if self.game_over: return

        user_input = self.entry.get().strip().title()
        if not user_input: return

        guess_elem = next((e for e in ELEMENTS if e.name == user_input or e.symbol == user_input), None)

        if not guess_elem:
            messagebox.showerror("Error", "Element not found in database!\nCheck spelling.")
            return

        self.attempts += 1
        self.update_status()
        
        self.entry.delete(0, tk.END)

        feedback = []
        is_win = False
        
        if guess_elem.atomic_number == self.target.atomic_number:
            is_win = True
            msg_color = "success"
            result_text = "CORRECT MATCH!"
        else:
            msg_color = "error"

            if guess_elem.atomic_number < self.target.atomic_number:
                feedback.append(f"Go HIGHER (Target > {guess_elem.atomic_number})")
            else:
                feedback.append(f"Go LOWER (Target < {guess_elem.atomic_number})")
            

            if guess_elem.group_id == self.target.group_id:
                feedback.append("MATCH: Correct Group")
            if guess_elem.period == self.target.period:
                feedback.append("MATCH: Correct Period")
                
            result_text = " | ".join(feedback)


        self.history_text.config(state="normal")
        self.history_text.insert(tk.END, f"[{self.attempts}] {guess_elem.symbol} ({guess_elem.name}): ", "info")
        self.history_text.insert(tk.END, f"{result_text}\n", msg_color)
        self.history_text.see(tk.END)
        self.history_text.config(state="disabled")


        self.hint_label.config(text=self.get_hint(), fg=self.accent_color)

 
        if is_win:
            self.end_game(True)
        elif self.attempts >= self.max_attempts:
            self.end_game(False)

    def end_game(self, won):
        self.game_over = True
        self.entry.config(state="disabled")
        self.guess_btn.config(state="disabled", bg="#555555")
        
        if won:
            self.hint_label.config(text=f"SUCCESS! Target was {self.target.name}.", fg=self.success_color)
            messagebox.showinfo("Victory", f"Congratulations! You found {self.target.name} in {self.attempts} attempts.")
        else:
            self.hint_label.config(text=f"FAILURE. Target was {self.target.name}.", fg=self.error_color)
            messagebox.showinfo("Game Over", f"Out of attempts! The element was {self.target.name} ({self.target.symbol}).")

if __name__ == "__main__":
    root = tk.Tk()
    app = ElementGameGUI(root)
    root.mainloop()