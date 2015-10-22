from age_calc.calculator import Calculator
from age_calc.gui import CalcGui
from tkinter import *
import argparse
"""Calculate Ages"""


def _launch():
    parser = argparse.ArgumentParser(
        prog='python -m age_calc',
        description=__doc__,
    )
    parser.add_argument('-gui', '--use-gui', action='store_true', default=False)
    parser.add_argument('-dob', '--date-of-birth', action='store', default=None, nargs=1)
    parser.add_argument('-v', '--version', action='store_true', default=False)
    args = parser.parse_args()
    if args.version:
        print('Age Calculator version 1.0')
        exit(0)
    if args.use_gui:
        root = Tk()
        root.wm_title('Calculate Age')
        app = CalcGui(root)
        root.mainloop()
    elif args.date_of_birth:
        calc = Calculator()
        print('As of today the age is: {age}'.format(age=calc.age_as_of_today(dob=args.date_of_birth[0])))
    else:
        parser.print_usage()

if __name__ == '__main__':
    _launch()
