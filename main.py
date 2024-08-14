import tkinter as tk
from tkinter import ttk
import tkinter.font as font

GREEN = "#339966"
BLUE = "#33cccc"
COFFEE = "#c2c2a3"


class HomeworkApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Homework Application")

        self.columnconfigure(0, weight=1)

        self.button_font = font.Font(family="Helvetica", size=12, weight="bold")
        self.text_font = font.Font(family="Courier", size=12)

        style = ttk.Style(self)
        style.configure("TButton", font=self.button_font)

        self.button_frame = ttk.Frame(self)
        self.button_frame.grid(pady=20, padx=20)

        self.first_button = ttk.Button(self.button_frame, text="Homework1", command=self.show_homework_1, style="TButton")
        self.first_button.grid(row=0, column=0, padx=10, pady=10)

        self.second_button = ttk.Button(self.button_frame, text="Homework2", command=self.show_homework_2, style="TButton")
        self.second_button.grid(row=0, column=1, padx=10, pady=10)

        self.third_button = ttk.Button(self.button_frame, text="Homework3", command=self.show_homework_3, style="TButton")
        self.third_button.grid(row=0, column=2, padx=10, pady=10)

        self.question_text = tk.Text(self, wrap=tk.WORD, width=50, height=3, font=self.text_font, bg=COFFEE)
        self.question_text.grid(pady=10)

        self.answer_text = tk.Text(self, wrap=tk.WORD, width=50, height=10, font=self.text_font, bg=COFFEE)
        self.answer_text.grid()

    def show_homework_1(self):
        self.answer_text.delete(1.0, tk.END)
        self.question_text.delete(1.0, tk.END)
        question_1 = "Question 1: Write a python program that show a fibonice sequeance:"
        homework1_content = """
        Answer:
        a,b = 0,1
        for i in range(10):
        print(a)
        a,b = b,a+b
        """
        self.answer_text.insert(1.0, homework1_content)
        self.question_text.insert(1.0, question_1)

    def show_homework_2(self):
        self.answer_text.delete(1.0, tk.END)
        self.question_text.delete(1.0, tk.END)
        question_2 = "Question 2: Write a python program that show a factorial sequeance:"
        homework1_content = """
        def fact(x):
        if x<0:
        print("negative number do not have
        factorial")
        if x==0 or x==1:
        return 1
        if x>0:
        return x*fact(x-1)"""
        self.answer_text.insert(tk.END, homework1_content)
        self.question_text.insert(1.0, question_2)

    def show_homework_3(self):
        self.answer_text.delete(1.0, tk.END)
        self.question_text.delete(1.0, tk.END)
        question_3 = "Question 3: Built in functions:"
        homework1_content = """
        1: (abs(x)): return the absolute value
        of a number.
        2: bin(x): convert an integer number to
        binary string.
        3: dict[(args)]: create a new data
        dictionary.
        4: float(x): convert a string or number
        to floating point number.
        5: hex(x): convert an integer number to
        a hexadecimel string.
        6: id(object): return the identity of
        an object.
        7: input():
        8: int():
        9: len():
        10: local():
        11: long():
        12: map():
        13: max():
        14: min():
        15: next():
        """
        self.answer_text.insert(tk.END, homework1_content)
        self.question_text.insert(tk.END, question_3)

window = HomeworkApp()
window.mainloop()
        
















