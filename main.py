from tkinter import *
import tkinter.messagebox

root = Tk()
root.title('Project 2')
root.geometry('400x200')


def clear():
    input_amount.delete(0, END)
    output_result.delete(0, END)


def convert():
    from forex_python.converter import CurrencyRates
    rate = CurrencyRates()
    from_currency = menu.get()
    to_currency = menu2.get()

    if input_amount.get() == "":
        tkinter.messagebox.showinfo('Error!', '\n Please a valid amount.')
    elif from_currency == to_currency:
        tkinter.messagebox.showinfo("Error!",
                                    "Currency Not Selected.\n Please select FROM and TO Currency form menu.")

    else:
        new_amt = rate.convert(from_currency, to_currency, float(input_amount.get()))
        new_amount = float(f'{new_amt:.3}')
        output_result.insert(0, str(new_amount))


CurrencyList = ['AUD', 'INR', 'USD', 'KRW', 'BRL', 'CAD', 'CNY', 'DKK', 'EUR', 'JPN', 'CZK', 'THB', 'NZD', 'MXN', ]

menu = StringVar()
menu.set("From")

menu2 = StringVar()
menu2.set("To")

appName = Label(text='Currency Converter', font=('Arial', 15))
appName.grid(row=1, column=1, padx=10)

from_dropmenu = OptionMenu(root, menu, *CurrencyList)
from_dropmenu.grid(row=2, column=1, pady=5)

to_dropmenu = OptionMenu(root, menu2, *CurrencyList)
to_dropmenu.grid(row=3, column=1, pady=5)

input_amount = Entry(root)
input_amount.grid(row=2, column=2, pady=5, padx=5)

output_result = Entry(root)
output_result.grid(row=3, column=2, padx=5)

convert_button = Button(root, text="Convert", command=convert)
convert_button.grid(row=4, column=1, pady=5)

clear_button = Button(root, text='Clear', command=clear)
clear_button.grid(row=4, column=2)

root.mainloop()
