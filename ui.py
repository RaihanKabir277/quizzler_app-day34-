from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20 , pady=20, bg=THEME_COLOR)
        self.score_label = Label(text="Score : 0", fg="white", bg=THEME_COLOR,font='Helvetica 18 bold')
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=400, height=300, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(200,150,width=380, text="some question text", fill="black", font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_img = PhotoImage(file="images/true.png")
        false_img = PhotoImage(file="images/false.png")
        self.true_btn = Button(image=true_img, highlightthickness=0, command=self.check_true)
        self.true_btn.grid(row=2, column=0)
        self.false_btn = Button(image=false_img, highlightthickness=0, command=self.check_false)
        self.false_btn.grid(row=2, column=1)
        self.get_next_question()

        self.window.mainloop()
    
    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}/{self.quiz.question_number}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text = "You reached the end of the question")
            self.true_btn.config(state="disabled")
            self.false_btn.config(state="disabled")

    def check_true(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)
    def check_false(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)

    

