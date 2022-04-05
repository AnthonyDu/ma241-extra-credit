from tkinter import *
from tkinter import messagebox
from pkg.fx import *
from decimal import *
from pkg.integral_estimator import *

class IntegralEstimatorGUI:

    def run(self):
        self.root = Tk()
        self.root.title("Integral Estimator")
        self.root.bind('<Return>', lambda event: self.calculate())
        open("geometry.config", "a").close()
        with open("geometry.config", "r") as conf:
            self.root.geometry(conf.read())

        self.root.resizable(False, False)

        self.interface()

        self.root.protocol("WM_DELETE_WINDOW", self.on_close)
        self.root.mainloop()

    def interface(self):
        master = Frame(self.root)

        welcome = Label(master, text="Welcome to Integral Estimator!")
        welcome.pack()

        rules = Frame(master)

        self.rule = StringVar(value="T")
        rule_radio1 = Radiobutton(rules, text="Trapezoidal Rule", variable=self.rule, value="T")
        rule_radio2 = Radiobutton(rules, text="Simpson's Rule", variable=self.rule, value="S")
        rule_radio1.grid(row=0, column=0)
        rule_radio2.grid(row=0, column=1)

        rules.pack()

        entries = Frame(master)

        self.fx = StringVar()
        fx_label = Label(entries, text="f(x) = ")
        fx_label.grid(row=2, column=0)
        fx_entry = Entry(entries, textvariable=self.fx)
        fx_entry.grid(row=2, column=1)
        fx_entry.focus_set()

        self.a = StringVar()
        a_label = Label(entries, text="a = ")
        a_label.grid(row=3, column=0)
        a_entry = Entry(entries, textvariable=self.a)
        a_entry.grid(row=3, column=1)

        self.b = StringVar()
        b_label = Label(entries, text="b = ")
        b_label.grid(row=4, column=0)
        b_entry = Entry(entries, textvariable=self.b)
        b_entry.grid(row=4, column=1)

        self.n = StringVar()
        n_label = Label(entries, text="n = ")
        n_label.grid(row=5, column=0)
        n_entry = Entry(entries, textvariable=self.n)
        n_entry.grid(row=5, column=1)

        entries.pack()

        calc_button = Button(master, text="Compute", command=self.calculate)
        calc_button.pack()

        master.pack(padx=20, pady=20)

    def calculate(self):
        fx = Fx(self.fx.get())
        if not fx.is_valid_fx():
            messagebox.showwarning(message="The funtion of x you entered is invalid!")
            self.root.focus_get().focus_force()
            return

        try:
            a = Decimal(self.a.get())
            b = Decimal(self.b.get())
            n = Decimal(self.n.get())
        except InvalidOperation:
            messagebox.showwarning(message="Please enter a decimal number!")
            self.root.focus_get().focus_force()
            return

        if b < a:
            messagebox.showwarning(message="b must not be equal or less than a!")
            self.root.focus_get().focus_force()
            return

        if self.rule.get() == "S" and (n % 2 != 0 or n <= 0):
            messagebox.showwarning(message="n has to be a positive even number!")
            self.root.focus_get().focus_force()
            return
        elif n <= 0:
            messagebox.showwarning(message="n has to be a positive number!")
            self.root.focus_get().focus_force()
            return

        fxs = []
        for i in range(int(n) + 1):
            x = a + (b - a) / n * i
            fxs.append(fx.evaluate_fx(x))

        integration = IntegralEstimator(self.rule.get(), a, b, n, fxs)

        if integration.rule == "T":
            result = sympy_number_to_str(integration.trap_estimate())
            message = f"The Trapezoidal Rule estimation of the integral of {fx.get_fx()} from {a} to {b} is {result}"
            messagebox.showinfo(message=message)
            self.root.focus_get().focus_force()
        elif integration.rule == "S":
            result = sympy_number_to_str(integration.simp_estimate())
            message = f"The Simpson's Rule estimation of the integral of {fx.get_fx()} from {a} to {b} is {result}"
            messagebox.showinfo(message=message)
            self.root.focus_get().focus_force()


    def on_close(self):
        with open("geometry.config", "w") as conf:
            conf.write(f"+{self.root.winfo_x()}+{self.root.winfo_y()}")
        self.root.destroy()


IntegralEstimatorGUI().run()
