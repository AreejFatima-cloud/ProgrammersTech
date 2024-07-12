import tkinter as tk
from tkinter import ttk,messagebox
from PIL import Image, ImageTk
import random
import time
from quiz_data import quiz_data

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Game")
        self.root.geometry("800x600")

        # Load background image
        self.background_image = Image.open("quiz.PNG")
        self.background_image = self.background_image.resize((800, 600), Image.LANCZOS)
        self.background_photo = ImageTk.PhotoImage(self.background_image)

        # Create a label to hold the background image
        self.background_label = tk.Label(self.root, image=self.background_photo)
        self.background_label.place(relwidth=1, relheight=1)

        self.score = 0
        self.current_question = 0

        # Timer variables
        self.start_time = None
        self.end_time = None

        self.create_widgets()

        self.show_welcome_message()

    def create_widgets(self):
        # Create a label for the question text
        self.question_label = tk.Label(self.root, text="", wraplength=500, font=("Helvetica", 16), bg="#00032F", fg="white")
        self.question_label.place(x=150, y=50, width=500, height=50)

        # Create a frame for the answer buttons
        self.answers_frame = tk.Frame(self.root, bg="#00032F")
        self.answers_frame.place(x=150, y=150, width=300, height=200)

        self.answer_buttons = []
        for i in range(4):
            btn = ttk.Button(self.answers_frame, command=lambda i=i: self.check_answer(i))
            btn.pack(fill='x', pady=5)
            self.answer_buttons.append(btn)

        # Create a label for feedback
        self.feedback_label = tk.Label(self.root, text="", font=("Helvetica", 12), bg="#00032F", fg="white")
        self.feedback_label.place(x=150, y=350, width=300, height=30)

        # Create a button for the next question
        self.next_button = ttk.Button(self.root, text="Next", command=self.next_question, state=tk.DISABLED)
        self.next_button.place(x=250, y=400, width=100, height=30)

    def show_welcome_message(self):
        tk.messagebox.showinfo("Welcome", "Welcome to the Quiz Game!\nYou will be asked multiple-choice questions. Good luck!")
        self.start_time = time.time()
        self.show_question()

    def show_question(self):
        question = quiz_data[self.current_question]
        self.question_label.config(text=question["question"])
        random.shuffle(question["answers"])
        for i, answer in enumerate(question["answers"]):
            self.answer_buttons[i].config(text=answer, state=tk.NORMAL)
        self.feedback_label.config(text="")
        self.next_button.config(state=tk.DISABLED)

    def check_answer(self, index):
        question = quiz_data[self.current_question]
        selected_answer = self.answer_buttons[index].cget("text")
        if selected_answer == question["correct_answer"]:
            self.score += 1
            self.feedback_label.config(text="Correct!", fg="green")
        else:
            self.feedback_label.config(text=f"Incorrect! The correct answer is {question['correct_answer']}.", fg="red")

        for btn in self.answer_buttons:
            btn.config(state=tk.DISABLED)
        self.next_button.config(state=tk.NORMAL)

    def next_question(self):
        self.current_question += 1
        if self.current_question < len(quiz_data):
            self.show_question()
        else:
            self.end_time = time.time()
            total_time = self.end_time - self.start_time
            self.show_final_score(total_time)

    def show_final_score(self, total_time):
        dialog = tk.Toplevel(self.root)
        dialog.title("Quiz Completed")
        dialog.geometry("300x200")

        tk.Label(dialog, text=f"Final Score: {self.score}/{len(quiz_data)}\nTime taken: {total_time:.2f} seconds", font=("Helvetica", 12)).pack(pady=20)

        play_again_button = ttk.Button(dialog, text="Play Again", command=lambda: [dialog.destroy(), self.reset_quiz()])
        play_again_button.pack(side="left", padx=20, pady=20)

        exit_button = ttk.Button(dialog, text="Exit", command=self.root.quit)
        exit_button.pack(side="right", padx=20, pady=20)

    def reset_quiz(self):
        self.score = 0
        self.current_question = 0
        self.start_time = time.time()
        self.show_question()

# Main
root = tk.Tk()
app = QuizApp(root)
root.mainloop()
