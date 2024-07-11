import tkinter as tk
from tkinter import ttk, messagebox
import random
from quiz_data import quiz_data
# Quiz data - questions and answers

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Game")
        self.root.geometry("600x400")

        self.score = 0
        self.current_question = 0

        self.create_widgets()

        self.show_welcome_message()

    def create_widgets(self):
        self.question_label = ttk.Label(self.root, text="", wraplength=500, font=("Helvetica", 16))
        self.question_label.pack(pady=20)

        self.answers_frame = ttk.Frame(self.root)
        self.answers_frame.pack(pady=20)

        self.feedback_label = ttk.Label(self.root, text="", font=("Helvetica", 12))
        self.feedback_label.pack(pady=10)

        self.next_button = ttk.Button(self.root, text="Next", command=self.next_question, state=tk.DISABLED)
        self.next_button.pack(pady=10)

    def show_welcome_message(self):
        messagebox.showinfo("Welcome to the Quiz Game",
                            "Welcome to the Quiz Game!\n\nRules:\n1. You will be asked multiple-choice questions.\n2. Select the correct answer.\n3. Your score will be displayed at the end.\n\nClick OK to start the quiz.")
        self.load_question()

    def load_question(self):
        if self.current_question < len(quiz_data):
            question_data = quiz_data[self.current_question]
            question = question_data["question"]
            answers = question_data["answers"]

            self.question_label.config(text=question)

            # Clear previous answers
            for widget in self.answers_frame.winfo_children():
                widget.destroy()

            # Shuffle answers
            random.shuffle(answers)

            # Create answer buttons
            for answer in answers:
                answer_button = ttk.Button(self.answers_frame, text=answer,
                                           command=lambda ans=answer: self.check_answer(ans, question_data["correct_answer"]))
                answer_button.pack(pady=5)

            # Disable next button initially
            self.next_button.config(state=tk.DISABLED)
            self.feedback_label.config(text="")
        else:
            self.display_result()

    def check_answer(self, selected_answer, correct_answer):
        if selected_answer == correct_answer:
            self.score += 1
            self.feedback_label.config(text="Correct!", foreground="green")
        else:
            self.feedback_label.config(text=f"Incorrect! Correct answer is: {correct_answer}", foreground="red")

        # Disable answer buttons after selection
        for widget in self.answers_frame.winfo_children():
            widget.config(state=tk.DISABLED)

        # Enable next button
        self.next_button.config(state=tk.NORMAL)

    def next_question(self):
        self.current_question += 1
        self.load_question()

    def display_result(self):
        messagebox.showinfo("Quiz Completed", f"Quiz Completed!\nYour score: {self.score}/{len(quiz_data)}")

        # Ask if the user wants to play again
        if messagebox.askyesno("Play Again?", "Do you want to play again?"):
            self.score = 0
            self.current_question = 0
            self.load_question()
        else:
            self.root.quit()

# Main function to start the quiz
def main():
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
