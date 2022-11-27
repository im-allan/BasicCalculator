import tkinter as tk
import tkinter.ttk as ttk
from tkinter import PhotoImage
import utils
import parser


class HoverButtonOperator(tk.Button):
    def __init__(self, master, **kw):
        tk.Button.__init__(self, master=master, **kw)
        self["background"] = "#3d2e2e"
        self["foreground"] = "#ffffff"
        self.defaultBackground = self["background"]
        self["font"] = ("Roboto", 12)

        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def on_enter(self, e):
        self['background'] = "#463737"

    def on_leave(self, e):
        self['background'] = self.defaultBackground


class HoverButtonNumber(tk.Button):
    def __init__(self, master, **kw):
        tk.Button.__init__(self, master=master, **kw)
        self["background"] = "#463737"
        self["foreground"] = "#ffffff"
        self.defaultBackground = self["background"]
        self["font"] = ("Roboto", 12)

        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def on_enter(self, e):
        self['background'] = "#3d2e2e"

    def on_leave(self, e):
        self['background'] = self.defaultBackground


class HoverButtonEqual(tk.Button):
    def __init__(self, master, **kw):
        tk.Button.__init__(self, master=master, **kw)
        self["background"] = "#f28065"
        self["foreground"] = "#703b2e"
        self.defaultBackground = self["background"]
        self["font"] = ("Roboto", 12)

        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def on_enter(self, e):
        self['background'] = "#ac5c4c"

    def on_leave(self, e):
        self['background'] = self.defaultBackground


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

        display = utils.CustomEntry(frame, font=("Roboto", 26), justify="right", bg="#271d21",
                                    fg="white", relief="flat", borderwidth=10, insertbackground="#271d21")
        display.insert(tk.END, 0)
        display.grid(row=2, column=0, columnspan=12, sticky="news", pady=1)


#  Functions


        def get_operation(operator):
            operator_length = len(operator)
            display.insert(MainApplication.i, operator)
            MainApplication.i += operator_length

        def get_number(n):
            if display.get() == "0":
                display.delete(0, tk.END)
            display.insert(MainApplication.i, n)
            MainApplication.i += 1

        def delete_character():
            display.delete(len(display.get())-1)

            if len(display.get()) == 0:
                display.insert(tk.END, 0)
                history.delete(0, tk.END)

        def clear_display():
            display.delete(0, tk.END)

        def get_square(operator):
            display_exp = display.get()

            if display_exp == "0":
                display.delete(0, tk.END)
                display.insert(tk.END, 0)

            elif len(display_exp) >= 1:
                operator_length = len(operator)
                display.insert(MainApplication.i, operator)
                MainApplication.i += operator_length
                get_result()
                history.delete(0, tk.END)
                history.insert(0, f"{display_exp}{operator} =")

        def get_result():

            display_state = display.get()

            if "÷" in display_state:
                display_state = display_state.replace("÷", "/")
            elif "²" in display_state:
                display_state = display_state.replace("²", "**2")
            else:
                display_state = display.get()

            try:
                math_expression = parser.expr(display_state).compile()
                result = eval(math_expression)
                clear_display()
                history.delete(0, tk.END)
                history.insert(0, f"{display_state} =")
                display.insert(0, result)
            except Exception:
                clear_display()
                history.delete(0, tk.END)
                display.insert(0, "Error")
                # Buttons
        percentage = PhotoImage(
            file=r"assets\percentage-32.png").subsample(2, 2)
        label_percentage = tk.Label(image=percentage)
        label_percentage.image = percentage
        HoverButtonOperator(frame, image=percentage, borderwidth=0,
                            command=lambda: get_operation("%")).grid(row=3, column=0, columnspan=3, sticky="news", padx=1, pady=1)

        HoverButtonOperator(frame, text="CE", borderwidth=0).grid(
            row=3, column=3, columnspan=3, sticky="news", padx=1, pady=1)
        HoverButtonOperator(frame, text="C", borderwidth=0).grid(
            row=3, column=6, columnspan=3, sticky="news", padx=1, pady=1)

        delete = PhotoImage(file=r"assets\delete-48.png").subsample(3, 3)
        label_delete = tk.Label(image=delete)
        label_delete.image = delete

        HoverButtonOperator(frame, image=delete, borderwidth=0,
                            command=lambda: delete_character()).grid(row=3, column=9, columnspan=3, sticky="news", padx=1, pady=1)

        plus_x = PhotoImage(file=r"assets\one-slash-x.png").subsample(1, 2)
        label_plus_x = tk.Label(image=plus_x)
        label_plus_x.image = plus_x
        HoverButtonOperator(frame, image=plus_x, borderwidth=0, command=lambda: get_operation(
            "¹∕×")).grid(row=4, column=0, columnspan=3, sticky="news", padx=1, pady=1)

        square = PhotoImage(file=r"assets\square-67.png").subsample(3, 3)
        label_square = tk.Label(image=square)
        label_square.image = square
        HoverButtonOperator(frame, image=square, borderwidth=0,
                            command=lambda: get_square("²")).grid(row=4, column=3, columnspan=3, sticky="news", padx=1, pady=1)

        square_root = PhotoImage(
            file=r"assets\square-root-67.png").subsample(3, 3)
        label_square_root = tk.Label(image=square_root)
        label_square_root.image = square_root
        HoverButtonOperator(frame, image=square_root, borderwidth=0,
                            command=lambda: get_operation("²√×")).grid(row=4, column=6, columnspan=3, sticky="news", padx=1, pady=1)

        divide = PhotoImage(file=r"assets\divide-32.png").subsample(2, 2)
        label_divide = tk.Label(image=divide)
        label_divide.image = divide
        HoverButtonOperator(frame, image=divide, borderwidth=0,
                            command=lambda: get_operation("÷")).grid(row=4, column=9, columnspan=3, sticky="news", padx=1, pady=1)

        HoverButtonNumber(frame, text="7", borderwidth=0,
                          command=lambda: get_number(7)).grid(row=5, column=0, columnspan=3, sticky="news", padx=1, pady=1)
        HoverButtonNumber(frame, text="8", borderwidth=0,
                          command=lambda: get_number(8)).grid(row=5, column=3, columnspan=3, sticky="news", padx=1, pady=1)
        HoverButtonNumber(frame, text="9", borderwidth=0,
                          command=lambda: get_number(9)).grid(row=5, column=6, columnspan=3, sticky="news", padx=1, pady=1)
        HoverButtonOperator(frame, text="⨉", borderwidth=0).grid(
            row=5, column=9, columnspan=3, sticky="news", padx=1, pady=1)

        HoverButtonNumber(frame, text="4", borderwidth=0,
                          command=lambda: get_number(4)).grid(row=6, column=0, columnspan=3, sticky="news", padx=1, pady=1)
        HoverButtonNumber(frame, text="5", borderwidth=0,
                          command=lambda: get_number(5)).grid(row=6, column=3, columnspan=3, sticky="news", padx=1, pady=1)
        HoverButtonNumber(frame, text="6", borderwidth=0,
                          command=lambda: get_number(6)).grid(row=6, column=6, columnspan=3, sticky="news", padx=1, pady=1)

        subtract = PhotoImage(file=r"assets\subtract-32.png").subsample(2, 2)
        label_subtract = tk.Label(image=subtract)
        label_subtract.image = subtract
        HoverButtonOperator(frame, image=subtract, borderwidth=0,).grid(
            row=6, column=9, columnspan=3, sticky="news", padx=1, pady=1)

        HoverButtonNumber(frame, text="1", borderwidth=0,
                          command=lambda: get_number(1)).grid(row=7, column=0, columnspan=3, sticky="news", padx=1, pady=1)
        HoverButtonNumber(frame, text="2", borderwidth=0,
                          command=lambda: get_number(2)).grid(row=7, column=3, columnspan=3, sticky="news", padx=1, pady=1)
        HoverButtonNumber(frame, text="3", borderwidth=0,
                          command=lambda: get_number(3)).grid(row=7, column=6, columnspan=3, sticky="news", padx=1, pady=1)

        addition = PhotoImage(file=r"assets\plus-32.png").subsample(2, 2)
        label_addition = tk.Label(image=addition)
        label_addition.image = addition
        HoverButtonOperator(frame, image=addition, borderwidth=0).grid(
            row=7, column=9, columnspan=3, sticky="news", padx=1, pady=1)

        HoverButtonNumber(frame, text="+/-", borderwidth=0).grid(row=8,
                                                                 column=0, columnspan=3, sticky="news", padx=1, pady=1)
        HoverButtonNumber(frame, text="0", borderwidth=0,
                          command=lambda: get_number(0)).grid(row=8, column=3, columnspan=3, sticky="news", padx=1, pady=1)
        HoverButtonNumber(frame, text=",", borderwidth=0).grid(
            row=8, column=6, columnspan=3, sticky="news", padx=1, pady=1)

        equal = PhotoImage(file=r"assets\equal-32.png").subsample(2, 2)
        label_equal = tk.Label(image=equal)
        label_equal.image = equal
        HoverButtonEqual(frame, image=equal, borderwidth=0, command=lambda: get_result()).grid(
            row=8, column=9, columnspan=3, sticky="news", padx=1, pady=1)


# Responsive Design

        frame.columnconfigure(tuple(range(12)), weight=1)
        frame.rowconfigure(tuple(range(9)), weight=1)


if __name__ == "__main__":
    root = tk.Tk()

    MainApplication(root)
    root.mainloop()
