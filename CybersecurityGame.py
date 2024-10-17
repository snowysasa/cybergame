import json
import random
import tkinter as tk
from tkinter import messagebox

# Load questions from JSON file
def load_questions(filename):
    with open(filename, 'r') as file:
        questions = json.load(file)
    return questions

def save_score(score):
    with open("high_scores.txt", "a") as file:
        file.write(f"{score}\n")

def load_high_scores():
    try:
        with open("high_scores.txt", "r") as file:
            scores = [int(line.strip()) for line in file]
        return scores
    except FileNotFoundError:
        return []

class CyberSecurityGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Cybersecurity Training")
        self.root.geometry("500x400")
        self.root.configure(bg="#0f1b0f")

        # Game Title
        self.title_label = tk.Label(root, text="Cybersecurity Training", font=("Comic Sans MS", 28, "bold"),
                                     fg="yellow", bg="#0f1b0f", bd=5, relief=tk.RAISED)
        self.title_label.pack(pady=20)

        # Instruction
        self.instructions = tk.Label(root, text="Choose a Mode to Start:", font=("Arial", 16), fg="white", bg="#0f1b0f")
        self.instructions.pack(pady=10)

        # Buttons for Game Modes
        self.quiz_button = tk.Button(root, text="Quiz Mode", font=("Arial", 16), bg="green", fg="white", command=self.start_quiz)
        self.quiz_button.pack(pady=10)

        self.command_button = tk.Button(root, text="Command Mode", font=("Arial", 16), bg="green", fg="white", command=self.start_command)
        self.command_button.pack(pady=10)

        # Exit Button
        self.exit_button = tk.Button(root, text="Exit", font=("Arial", 16), bg="red", fg="white", command=root.quit)
        self.exit_button.pack(pady=10)

    def start_quiz(self):
        self.quiz_window = tk.Toplevel(self.root)
        self.quiz_window.title("Quiz Mode")
        self.quiz_window.geometry("500x400")
        self.quiz_window.configure(bg='#1a3d1a')

        self.quiz_label = tk.Label(self.quiz_window, text="Welcome to Quiz Mode", font=("Arial", 18), fg="lime", bg='#1a3d1a')
        self.quiz_label.pack(pady=20)

        # Load Questions from JSON file
        self.questions = load_questions('questions.json')  # Load from your JSON file
        random.shuffle(self.questions)
        self.current_question = 0
        self.score = 0
        self.time_left = 300  # 5 minutes timer
        self.timer_label = tk.Label(self.quiz_window, text=f"Time Left: {self.time_left // 60}:{self.time_left % 60:02d}",
                                     font=("Arial", 14), fg="white", bg='#1a3d1a')
        self.timer_label.pack(pady=20)

        self.question_label = tk.Label(self.quiz_window, font=("Arial", 14), fg="white", bg='#1a3d1a')
        self.question_label.pack(pady=10)

        self.option_vars = tk.StringVar()
        self.option_buttons = []  # Store reference to option buttons

        self.submit_button = tk.Button(self.quiz_window, text="Submit", command=self.check_answer, bg="green", fg="white")
        self.submit_button.pack(pady=10)

        self.update_timer()
        self.display_question()

    def update_timer(self):
        if self.time_left > 0:
            self.time_left -= 1
            self.timer_label.config(text=f"Time Left: {self.time_left // 60}:{self.time_left % 60:02d}")
            self.quiz_window.after(1000, self.update_timer)
        else:
            self.show_score()  # End the quiz when the timer runs out

    def display_question(self):
        if self.current_question < len(self.questions):
            q = self.questions[self.current_question]
            self.question_label.config(text=q["question"])

            # Clear previous options
            for button in self.option_buttons:
                button.destroy()
            self.option_buttons.clear()

            # Create new option buttons
            for option in q["options"]:
                radio_button = tk.Radiobutton(self.quiz_window, text=option, variable=self.option_vars, value=option, font=("Arial", 12), fg="lime", bg='#1a3d1a')
                radio_button.pack()
                self.option_buttons.append(radio_button)  # Store the button reference

        else:
            self.show_score()

    def check_answer(self):
        selected_option = self.option_vars.get()
        correct_answer = self.questions[self.current_question]["answer"]
        if selected_option == correct_answer:
            self.score += 1
            messagebox.showinfo("Correct!", "You got it right!")
        else:
            messagebox.showinfo("Wrong!", f"The correct answer was: {correct_answer}.")
        self.current_question += 1
        self.display_question()

    def show_score(self):
        save_score(self.score)
        high_scores = load_high_scores()
        high_scores.sort(reverse=True)
        high_scores_display = "\n".join(str(score) for score in high_scores[:5])
        
        messagebox.showinfo("Quiz Over", f"Your score: {self.score}/{len(self.questions)}\n\nTop Scores:\n{high_scores_display}")
        self.quiz_window.destroy()

    def start_command(self):
        self.command_window = tk.Toplevel(self.root)
        self.command_window.title("Command Mode")
        self.command_window.geometry("500x400")
        self.command_window.configure(bg='#1a3d1a')

        self.command_label = tk.Label(self.command_window, text="Command Mode: Enter commands to solve scenarios", font=("Arial", 14), fg="lime", bg='#1a3d1a')
        self.command_label.pack(pady=10)

        self.scenario_label = tk.Label(self.command_window, text="Scenario 1: Check current user", font=("Arial", 12), fg="white", bg='#1a3d1a')
        self.scenario_label.pack(pady=10)

        self.command_entry = tk.Entry(self.command_window, font=("Arial", 12), width=50)
        self.command_entry.pack(pady=10)

        self.submit_button = tk.Button(self.command_window, text="Submit Command", command=self.check_command, bg="green", fg="white")
        self.submit_button.pack(pady=10)

        self.scenario_step = 0

    def check_command(self):
        command = self.command_entry.get()

        if self.scenario_step == 0 and command == "whoami":
            self.command_success("You are logged in as user!")
            self.scenario_step += 1
            self.scenario_label.config(text="Scenario 2: Check for sudo privileges.")
        elif self.scenario_step == 1 and command == "sudo -l":
            self.command_success("You have sudo privileges!")
            self.scenario_step += 1
            self.scenario_label.config(text="Scenario 3: Exit the command line.")
        elif self.scenario_step == 2 and command == "exit":
            self.command_success("You have exited the command line.")
            self.scenario_step += 1
            self.scenario_label.config(text="All scenarios complete.")
        else:
            messagebox.showinfo("Incorrect Command", "Try again!")

    def command_success(self, message):
        messagebox.showinfo("Success", message)

if __name__ == "__main__":
    root = tk.Tk()
    game = CyberSecurityGame(root)
    root.mainloop()