import tkinter as tk
from tkinter import PhotoImage
import utils
import parser
import math
import re


class MainApplication(tk.Frame):
    i = 0

    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent


# Global Settings

        parent.title("Calculator")
        parent.geometry("320x500")


# Grid Settings

        frame = tk.Canvas(root, bg="#271d21", highlightthickness=0)
        root.rowconfigure(0, weight=1)
        root.columnconfigure(0, weight=1)

        grid = tk.Frame(frame, padx=10, pady=10, bg="#271d21")
        grid.grid(sticky="news", column=0, row=10)

        frame.grid(row=0, column=0, sticky="news")
        frame.rowconfigure(8, weight=1)
        frame.columnconfigure(0, weight=1)


# Head

        tk.Label(frame, text="Standard", font=("Roboto", 18), justify="left",
                 bg="#271d21", fg="white").grid(row=0, column=1, columnspan=4, sticky="news")

        history = tk.Entry(frame, font=("Roboto", 11), justify="right", bg="#271d21",
                           fg="white", relief="flat", borderwidth=10, insertbackground="#271d21", highlightthickness=0)
        history.grid(row=1, column=0, columnspan=12,
                     sticky="ew", pady=0, ipady=0)

        display = utils.CustomEntry(frame, font=("Roboto", 22), justify="right", bg="#271d21",
                                    fg="white", relief="flat", borderwidth=10, insertbackground="#271d21")
        display.insert(tk.END, 0)
        display.grid(row=2, column=0, columnspan=12, sticky="news", pady=1)


#  Functions

# Clear functions

        def clear_display():
            display.delete(0, tk.END)

        def clear_history():
            history.delete(0, tk.END)

        def clear_entry():
            display.delete(0, tk.END)
            display.insert(tk.END, 0)

        def clear_all():
            clear_entry()
            clear_history()

        def delete_character():
            display.delete(len(display.get())-1)

            if len(display.get()) == 0:
                display.insert(tk.END, 0)
                clear_history()


# Getters functions


        def get_operation(operator):
            if history.get() in '=':
                history.insert(0, f"{display.get()} {operator}")
            else:
                history.delete(0, tk.END)
                history.insert(0, f"{display.get()} {operator}")

        def get_number(n):
            if display.get() == "0":
                display.delete(0, tk.END)

            if history.get() == '':
                display.insert(tk.END, n)

            elif history.get() != '':
                display.delete(0, tk.END)
                display.insert(tk.END, n)

        def get_square(operator):
            display_exp = display.get()

            if display_exp == "0":
                pass

            elif len(display_exp) >= 1:
                history.delete(0, tk.END)
                history.insert(0, f"{display_exp}{operator}")
                clear_display()
                get_result()

        def get_square_root(operator):
            display_exp = display.get()

            if display_exp == "0":
                pass

            elif len(display_exp) >= 1:

                try:
                    display.insert(0, operator)
                    clear_display()
                    display_entry = round(math.sqrt(int(display_exp)), 6)
                    display.insert(0, display_entry)
                    history.delete(0, tk.END)
                    history.insert(0, f"{operator} {display_exp} =")
                except Exception:
                    clear_display()
                    history.delete(0, tk.END)
                    display.insert(0, "SyntaxError")

        def get_whole_part(operator):
            display_exp = display.get()

            try:
                if display.get() >= 1:
                    history.delete(0, tk.END)
                    history.insert(0, f"{operator}({display_exp})")
                    clear_display()
                    get_result()

            except Exception:
                clear_display()
                history.delete(0, tk.END)
                display.insert(0, "Can't be divided by zero")

        def get_percentage():
            history_exp = history.get()
            try:
                if len(history_exp) >= 1:
                    display_exp = display.get()

                    if display_exp != "0":
                        n = [int(s)
                             for s in history_exp.split() if s.isdigit()]
                        percent = parser.expr(
                            f"{n[0]} * {display_exp} / 100").compile()
                        result = round(eval(percent), 6)
                        history.delete(0, tk.END)
                        history.insert(0, f"{history_exp} {result}")

                        history_result = round(
                            eval(parser.expr(history.get()).compile()), 6)
                        display.delete(0, tk.END)
                        display.insert(0, history_result)
                else:
                    clear_entry()
            except:
                clear_entry()

        def change_sym():
            display_exp = display.get()
            try:
                if len(display_exp) >= 1:
                    if "-" not in display_exp:
                        display.insert(0, "-")
                    else:
                        display.delete(0)

            except:
                clear_entry()

# Result functions

        def get_result():

            history_state = history.get()
            display_state = display.get()
            if "÷" in history_state:
                history_entry = history_state.replace("÷", "/")
            elif "²" in history_state:
                history_entry = history_state.replace("²", "**2")
            elif "×" in history_state:
                history_entry = history_state.replace("×", "*")
            else:
                history_entry = history.get()

            try:

                if "**2" in history_entry == True:

                    math_expression = parser.expr(
                        history_entry).compile()
                    result = round(eval(math_expression), 6)
                    clear_display()
                    history.delete(0, tk.END)
                    history.insert(0, f"{history_state} =")

                if "1/" in history_entry == True:

                    math_expression = parser.expr(
                        history_entry).compile()
                    result = round(eval(math_expression), 6)
                    clear_display()
                    history.delete(0, tk.END)
                    history.insert(0, f"{history_state} =")

                else:
                    math_expression = parser.expr(
                        history_entry + display_state).compile()

                    result = round(eval(math_expression), 6)

                    clear_display()
                    history.delete(0, tk.END)
                    history.insert(0, f"{history_state} {display_state} =")

                display.insert(0, result)
            except Exception:
                clear_display()
                history.delete(0, tk.END)
                display.insert(0, "SyntaxError")


# Buttons

        percentage = PhotoImage(
            file=r"assets\percentage-32.png").subsample(2, 2)
        label_percentage = tk.Label(image=percentage)
        label_percentage.image = percentage
        utils.HoverButtonOperator(frame, image=percentage, borderwidth=0,
                                  command=lambda: get_percentage()).grid(row=3, column=0, columnspan=3, sticky="news", padx=1, pady=1)

        utils.HoverButtonOperator(frame, text="CE", borderwidth=0, command=lambda: clear_entry()).grid(
            row=3, column=3, columnspan=3, sticky="news", padx=1, pady=1)
        utils.HoverButtonOperator(frame, text="C", borderwidth=0, command=lambda: clear_all()).grid(
            row=3, column=6, columnspan=3, sticky="news", padx=1, pady=1)

        delete = PhotoImage(file=r"assets\delete-48.png").subsample(3, 3)
        label_delete = tk.Label(image=delete)
        label_delete.image = delete

        utils.HoverButtonOperator(frame, image=delete, borderwidth=0,
                                  command=lambda: delete_character()).grid(row=3, column=9, columnspan=3, sticky="news", padx=1, pady=1)

        plus_x = PhotoImage(file=r"assets\one-slash-x.png").subsample(1, 2)
        label_plus_x = tk.Label(image=plus_x)
        label_plus_x.image = plus_x
        utils.HoverButtonOperator(frame, image=plus_x, borderwidth=0, command=lambda: get_whole_part(
            "1/")).grid(row=4, column=0, columnspan=3, sticky="news", padx=1, pady=1)

        square = PhotoImage(file=r"assets\square-67.png").subsample(3, 3)
        label_square = tk.Label(image=square)
        label_square.image = square
        utils.HoverButtonOperator(frame, image=square, borderwidth=0,
                                  command=lambda: get_square("²")).grid(row=4, column=3, columnspan=3, sticky="news", padx=1, pady=1)

        square_root = PhotoImage(
            file=r"assets\square-root-67.png").subsample(3, 3)
        label_square_root = tk.Label(image=square_root)
        label_square_root.image = square_root
        utils.HoverButtonOperator(frame, image=square_root, borderwidth=0,
                                  command=lambda: get_square_root("²√")).grid(row=4, column=6, columnspan=3, sticky="news", padx=1, pady=1)

        divide = PhotoImage(file=r"assets\divide-32.png").subsample(2, 2)
        label_divide = tk.Label(image=divide)
        label_divide.image = divide
        utils.HoverButtonOperator(frame, image=divide, borderwidth=0,
                                  command=lambda: get_operation("÷")).grid(row=4, column=9, columnspan=3, sticky="news", padx=1, pady=1)

        utils.HoverButtonNumber(frame, text="7", borderwidth=0,
                                command=lambda: get_number(7)).grid(row=5, column=0, columnspan=3, sticky="news", padx=1, pady=1)
        utils.HoverButtonNumber(frame, text="8", borderwidth=0,
                                command=lambda: get_number(8)).grid(row=5, column=3, columnspan=3, sticky="news", padx=1, pady=1)
        utils.HoverButtonNumber(frame, text="9", borderwidth=0,
                                command=lambda: get_number(9)).grid(row=5, column=6, columnspan=3, sticky="news", padx=1, pady=1)
        utils.HoverButtonOperator(frame, text="⨉", borderwidth=0, command=lambda: get_operation("×")).grid(
            row=5, column=9, columnspan=3, sticky="news", padx=1, pady=1)

        utils.HoverButtonNumber(frame, text="4", borderwidth=0,
                                command=lambda: get_number(4)).grid(row=6, column=0, columnspan=3, sticky="news", padx=1, pady=1)
        utils.HoverButtonNumber(frame, text="5", borderwidth=0,
                                command=lambda: get_number(5)).grid(row=6, column=3, columnspan=3, sticky="news", padx=1, pady=1)
        utils.HoverButtonNumber(frame, text="6", borderwidth=0,
                                command=lambda: get_number(6)).grid(row=6, column=6, columnspan=3, sticky="news", padx=1, pady=1)

        subtract = PhotoImage(file=r"assets\subtract-32.png").subsample(2, 2)
        label_subtract = tk.Label(image=subtract)
        label_subtract.image = subtract
        utils.HoverButtonOperator(frame, image=subtract, borderwidth=0, command=lambda: get_operation("-")).grid(
            row=6, column=9, columnspan=3, sticky="news", padx=1, pady=1)

        utils.HoverButtonNumber(frame, text="1", borderwidth=0,
                                command=lambda: get_number(1)).grid(row=7, column=0, columnspan=3, sticky="news", padx=1, pady=1)
        utils.HoverButtonNumber(frame, text="2", borderwidth=0,
                                command=lambda: get_number(2)).grid(row=7, column=3, columnspan=3, sticky="news", padx=1, pady=1)
        utils.HoverButtonNumber(frame, text="3", borderwidth=0,
                                command=lambda: get_number(3)).grid(row=7, column=6, columnspan=3, sticky="news", padx=1, pady=1)

        addition = PhotoImage(file=r"assets\plus-32.png").subsample(2, 2)
        label_addition = tk.Label(image=addition)
        label_addition.image = addition
        utils.HoverButtonOperator(frame, image=addition, borderwidth=0, command=lambda: get_operation("+")).grid(
            row=7, column=9, columnspan=3, sticky="news", padx=1, pady=1)

        utils.HoverButtonNumber(frame, text="+/-", borderwidth=0, command=lambda: change_sym()).grid(row=8,
                                                                                                     column=0, columnspan=3, sticky="news", padx=1, pady=1)
        utils.HoverButtonNumber(frame, text="0", borderwidth=0,
                                command=lambda: get_number(0)).grid(row=8, column=3, columnspan=3, sticky="news", padx=1, pady=1)
        utils.HoverButtonNumber(frame, text=",", borderwidth=0).grid(
            row=8, column=6, columnspan=3, sticky="news", padx=1, pady=1)

        equal = PhotoImage(file=r"assets\equal-32.png").subsample(2, 2)
        label_equal = tk.Label(image=equal)
        label_equal.image = equal
        utils.HoverButtonEqual(frame, image=equal, borderwidth=0, command=lambda: get_result()).grid(
            row=8, column=9, columnspan=3, sticky="news", padx=1, pady=1)


# Responsive Design

        frame.columnconfigure(tuple(range(12)), weight=1)
        frame.rowconfigure(tuple(range(9)), weight=1)


if __name__ == "__main__":
    root = tk.Tk()

    MainApplication(root)
    root.mainloop()
