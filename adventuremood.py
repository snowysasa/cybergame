import tkinter as tk
from tkinter import messagebox
import random

class CyberAwarenessGame:
    def __init__(self, master):
        self.master = master
        master.title("Cyber Awareness Adventure")
        master.geometry("500x400")
        
        self.avatar = None
        self.points = 0
        self.lives = 3
        self.mailbox = []
        
        self.create_widgets()
        self.choose_avatar()
        self.generate_mailbox()
        self.display_mailbox()

    def create_widgets(self):
        self.title_label = tk.Label(self.master, text="Welcome to Phishing Land!", font=("Arial", 16))
        self.title_label.pack(pady=10)

        self.mailbox_text = tk.Text(self.master, height=10, width=50, state=tk.DISABLED)
        self.mailbox_text.pack(pady=10)

        self.action_frame = tk.Frame(self.master)
        self.action_frame.pack(pady=5)

        self.mark_spam_button = tk.Button(self.action_frame, text="Mark as Spam", command=lambda: self.take_action("spam"))
        self.block_sender_button = tk.Button(self.action_frame, text="Block Sender", command=lambda: self.take_action("block"))
        self.report_button = tk.Button(self.action_frame, text="Report", command=lambda: self.take_action("report"))

        self.mark_spam_button.grid(row=0, column=0, padx=5)
        self.block_sender_button.grid(row=0, column=1, padx=5)
        self.report_button.grid(row=0, column=2, padx=5)

        self.score_label = tk.Label(self.master, text=f"Points: {self.points}  Lives: {self.lives}", font=("Arial", 12))
        self.score_label.pack(pady=10)

    def choose_avatar(self):
        avatar_choice = messagebox.askquestion("Choose Your Avatar", "Do you want to be a Cyber Defender?")
        if avatar_choice == 'yes':
            self.avatar = "Cyber Defender"
            messagebox.showinfo("Avatar Selected", f"You have chosen {self.avatar}!")

    def generate_mailbox(self):
        self.mailbox = [
            {"subject": "Your bank statement", "is_phishing": False},
            {"subject": "You've won a lottery!", "is_phishing": True},
            {"subject": "Meeting Reminder", "is_phishing": False},
            {"subject": "Urgent: Update your account info", "is_phishing": True},
            {"subject": "Your package is on the way", "is_phishing": False},
        ]
        random.shuffle(self.mailbox)

    def display_mailbox(self):
        self.mailbox_text.config(state=tk.NORMAL)
        self.mailbox_text.delete(1.0, tk.END)  # Clear previous text
        for idx, email in enumerate(self.mailbox):
            self.mailbox_text.insert(tk.END, f"{idx + 1}. {email['subject']}\n")
        self.mailbox_text.config(state=tk.DISABLED)

    def take_action(self, action):
        email_index = int(tk.simpledialog.askstring("Select Email", "Which email number do you want to act on?")) - 1

        if email_index < 0 or email_index >= len(self.mailbox):
            messagebox.showwarning("Invalid Selection", "Please select a valid email number.")
            return

        selected_email = self.mailbox[email_index]
        
        if action == "spam" and selected_email["is_phishing"]:
            self.points += 50
            messagebox.showinfo("Success", "Good job! You identified a phishing email.")
        else:
            messagebox.showerror("Oops!", "Oh no! You clicked on a legitimate email.")
            self.lives -= 1
            
        self.update_game_status()

    def update_game_status(self):
        self.score_label.config(text=f"Points: {self.points}  Lives: {self.lives}")
        if self.lives <= 0:
            messagebox.showerror("Game Over!", "Your system is compromised. Time to reboot your strategy!")
            self.master.quit()

if __name__ == "__main__":
    root = tk.Tk()
    game = CyberAwarenessGame(root)
    root.mainloop()
