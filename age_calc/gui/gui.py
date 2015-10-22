from tkinter import *
from tkinter import ttk
from datetime import date
from age_calc.calculator import Calculator


class CalcGui(object):
    def __init__(self, master):
        self.set_values()
        self.calc = Calculator()
        today = date.today()
        self.select_label = ttk.Label(master=master, text='DOB:')
        self.select_month = ttk.Combobox(master=master, textvariable=self.month, values=self.months)
        self.select_day = Spinbox(master=master, from_=1, to=31, textvariable=self.day)
        self.select_year = Spinbox(master=master, from_=1900, to=int(today.year), textvariable=self.year)
        # ttk.Combobox(master=master, textvariable=self.year, values=self.years)
        self.calc_age_button = ttk.Button(master=master, text='Calculate Age', command=self.age)
        self.age_label = ttk.Label(master=master, text='AGE NOT YET CALCULATED')
        self.select_label.grid(row=0, column=0)
        self.select_month.grid(row=0, column=1)
        self.select_day.grid(row=0, column=2)
        self.select_year.grid(row=0, column=3)
        self.calc_age_button.grid(row=0, column=4)
        self.age_label.grid(row=1, column=0, columnspan=5)
        self.set_defaults()

    def age(self):
        age = self.calculate_age()
        label_text = 'DOB: {m} {d}, {y}\tAGE:{a}'.format(
            m=self.month.get(),
            d=self.day.get(),
            y=self.year.get(),
            a=age
        )
        self.age_label.config(text=label_text)

    def set_values(self):
        self.month = StringVar()
        self.year = IntVar()
        self.day = IntVar()
        self.months = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')

    def set_defaults(self):
        self.select_month.set('Jun')
        self.day.set('9')
        self.year.set('1980')

    def calculate_age(self):
        """
        Calculate Age, Method to calculate the age today.
        :param birth_date: DATETIME
        :return: Int
        """
        dob_year = int(self.year.get())
        dob_month = int(self.months.index(self.month.get()) + 1)
        dob_day = int(self.day.get())
        return self.calc.age_as_of_today(month=dob_month, day=dob_day, year=dob_year)


def main():
    root = Tk()
    root.wm_title('Calculate Age')
    app = CalcGui(root)
    root.mainloop()

if __name__ == '__main__':
    main()
