from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        #SCORE
        self.score = Label(text=f"Score:{self.quiz.score}", fg="white", bg=THEME_COLOR)
        self.score.grid(column=1, row=0)

        #IMAGENS
        self.image_true = PhotoImage(file="images/true.png")
        self.image_false = PhotoImage(file="images/false.png")

        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.canvas.grid(columnspan=2, column=0, row=1, pady=50)

        self.text = self.canvas.create_text(150, 125, text="Some", width=280, font=("Arial", 20, "italic"))

        #BOTÕES
        self.true = Button(image=self.image_true, command=self.true_answer)
        self.true.grid(column=0, row=2)
        self.false = Button(image=self.image_false, command=self.wrong_answer)
        self.false.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.text, text=q_text)
        else:
            self.canvas.itemconfig(self.text, text="You've reached the end of the game!")
            self.true.config(state="disabled")
            self.false.config(state="disabled")

    def true_answer(self):
        is_right = self.quiz.check_answer(True)
        self.give_feedback(is_right)

    def wrong_answer(self):
        is_wrong = self.quiz.check_answer(False)
        self.give_feedback(is_wrong)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)

