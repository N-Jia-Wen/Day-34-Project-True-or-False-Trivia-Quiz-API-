from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250)
        # Making width of text slightly smaller than that of canvas causes text to wrap
        self.question_text = self.canvas.create_text(150, 125, width=280, text="Placeholder",
                                                     font=("Arial", 20, "italic"), fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        tick_img = PhotoImage(file="./images/true.png")
        self.tick = Button(image=tick_img, command=self.user_chose_true)
        self.tick.grid(row=2, column=0)

        cross_img = PhotoImage(file="./images/false.png")
        self.cross = Button(image=cross_img, command=self.user_chose_false)
        self.cross.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")

        if self.quiz.still_has_questions() is True:
            self.tick.config(state="active")
            self.cross.config(state="active")

            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)

        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.tick.config(state="disabled")
            self.cross.config(state="disabled")

    def user_chose_true(self):
        is_answer_correct = self.quiz.check_answer("True")
        self.give_feedback(is_answer_correct)

    def user_chose_false(self):
        is_answer_correct = self.quiz.check_answer("False")
        self.give_feedback(is_answer_correct)

    def give_feedback(self, is_answer_correct: bool):
        if is_answer_correct is True:
            self.canvas.config(bg="green")
        elif is_answer_correct is False:
            self.canvas.config(bg="red")

        self.tick.config(state="disabled")
        self.cross.config(state="disabled")
        self.window.after(1000, self.get_next_question)
