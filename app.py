import tkinter as tk
import tkinter.ttk as ttk



class MainApplication(tk.Frame):
    i = 0
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
    

# Global Settings 

        parent.title("Calculator")   
        parent.geometry("320x500")


# Grid Settings 

        frame = tk.Frame(root)

        root.rowconfigure(0, weight=1)
        root.columnconfigure(0, weight=1)        

        
        grid = tk.Frame(frame)
        grid.grid(sticky="news", column=0, row=12)

        frame.grid(row=0, column=0, sticky="news")
        frame.rowconfigure(12, weight=1)
        frame.columnconfigure(0, weight=1)

        
# Head

        label = tk.Label(frame, text="Lorem Ipsum", anchor="w", font=("Microsoft Sans Serif", 14), borderwidth=0)
        label.grid(row=0, column=2, columnspan=12, sticky="news")

        ttk.Style().configure('dis.TEntry', padding='0 0 10 0', borderwidth=0, border=0)
        display = ttk.Entry(frame, font=("Microsoft Sans Serif", 24), justify= "right", style='dis.TEntry')
        display.grid(row=2, column=0, columnspan=12, sticky="news")

        ttk.Style().configure('his.TEntry', padding='0 0 10 0', borderwidth=0, border=0)
        history = ttk.Entry(frame, font=("Microsoft Sans Serif", 12), justify="right", style='dis.TEntry')
        history.grid(row=1, column=0, columnspan=12, sticky="news")


#  Functions 

        def get_operation(operator):
                operator_length = len(operator)
                display.insert(MainApplication.i, operator)
                MainApplication.i+=operator_length
        
        def get_number(n):
                display.insert(MainApplication.i, n)
                MainApplication.i+=1

        def delete_character():
                display.delete(len(display.get())-1)


# Buttons 

        tk.Button(frame, text = "%", borderwidth=0, command=lambda: get_operation("%")).grid(row = 3, column = 0, columnspan=3, sticky="news")
        tk.Button(frame, text = "CE", borderwidth=0).grid(row = 3, column = 3, columnspan=3, sticky="news")
        tk.Button(frame, text = "C", borderwidth=0).grid(row = 3, column = 6, columnspan=3, sticky="news")
        tk.Button(frame, text = "⌫", borderwidth=0, command=lambda: delete_character()).grid(row = 3, column = 9, columnspan=3, sticky="news")

        tk.Button(frame, text = "¹∕×", borderwidth=0, command=lambda: get_operation("¹∕×")).grid(row = 4, column = 0, columnspan=3, sticky="news")
        tk.Button(frame, text = "×²", borderwidth=0, command=lambda: get_operation("×²")).grid(row = 4, column = 3, columnspan=3, sticky="news")
        tk.Button(frame, text = "²√×", borderwidth=0, command=lambda: get_operation("²√×")).grid(row = 4, column = 6, columnspan=3, sticky="news")
        tk.Button(frame, text = "÷", borderwidth=0, command=lambda: get_operation("÷")).grid(row = 4, column = 9, columnspan=3, sticky="news")

        tk.Button(frame, text = "7", borderwidth=0, command=lambda: get_number(7)).grid(row = 5, column = 0, columnspan=3, sticky="news")
        tk.Button(frame, text = "8", borderwidth=0, command=lambda: get_number(8)).grid(row = 5, column = 3, columnspan=3, sticky="news")
        tk.Button(frame, text = "9", borderwidth=0, command=lambda: get_number(9)).grid(row = 5, column = 6, columnspan=3, sticky="news")
        tk.Button(frame, text = "⨉", borderwidth=0).grid(row = 5, column = 9, columnspan=3, sticky="news")

        tk.Button(frame, text = "4", borderwidth=0, command=lambda: get_number(4)).grid(row = 5, column = 0, columnspan=3, sticky="news")
        tk.Button(frame, text = "5", borderwidth=0, command=lambda: get_number(5)).grid(row = 5, column = 3, columnspan=3, sticky="news")
        tk.Button(frame, text = "6", borderwidth=0, command=lambda: get_number(6)).grid(row = 5, column = 6, columnspan=3, sticky="news")
        tk.Button(frame, text = "-", borderwidth=0).grid(row = 5, column = 9, columnspan=3, sticky="news")

        tk.Button(frame, text = "1", borderwidth=0, command=lambda: get_number(1)).grid(row = 6, column = 0, columnspan=3, sticky="news")
        tk.Button(frame, text = "2", borderwidth=0, command=lambda: get_number(2)).grid(row = 6, column = 3, columnspan=3, sticky="news")
        tk.Button(frame, text = "3", borderwidth=0, command=lambda: get_number(3)).grid(row = 6, column = 6, columnspan=3, sticky="news")
        tk.Button(frame, text = "+", borderwidth=0).grid(row = 6, column = 9, columnspan=3, sticky="news")

        tk.Button(frame, text = "±", borderwidth=0).grid(row = 7, column = 0, columnspan=3, sticky="news")
        tk.Button(frame, text = "0", borderwidth=0, command=lambda: get_number(0)).grid(row = 7, column = 3, columnspan=3, sticky="news")
        tk.Button(frame, text = ",", borderwidth=0).grid(row = 7, column = 6, columnspan=3, sticky="news")
        tk.Button(frame, text = "=", borderwidth=0).grid(row = 7, column = 9, columnspan=3, sticky="news")


# Responsive Design 

        frame.columnconfigure(tuple(range(12)), weight=1)
        frame.rowconfigure(tuple(range(8)), weight=1)


if __name__ == "__main__":
    root = tk.Tk()

    MainApplication(root)
    root.mainloop()
