# Front end gui that opens GUIs for the various operations

from tkinter import *
from tkinter import messagebox
from tkinter import ttk

root = Tk()
root.style = ttk.Style()
root.style.theme_use('clam')
root.title('Point of Sale')

# Grid setup so elements resize with window
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

root.grid_rowconfigure(0, weight=0)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(3, weight=1)

# Label Creation
Label(root, anchor='center', text='Cashier').grid(row=0, column=0, sticky=EW)
Label(root, anchor='center', text='Manager').grid(row=0, column=1, sticky=EW)

# Button Creation
sale_btn = Button(root, anchor='center', text='Sale Processing').grid(row=1, column=0, sticky=NSEW)
returns_btn = Button(root, anchor='center', text='Returns Processing').grid(row=2, column=0, sticky=NSEW)
on_hand_btn = Button(root, anchor='center', text='OH Check').grid(row=3, column=0, sticky=NSEW)

sales_report_btn = Button(root, anchor='center', text='Sales Report').grid(row=1, column=1, sticky=NSEW)
schedule_btn = Button(root, anchor='center', text='Schedule').grid(row=2, column=1, sticky=NSEW)

root.mainloop()