# GUI opened for sale processing

from tkinter import *
from tkinter import messagebox
from tkinter import ttk

root = Tk()
root.style = ttk.Style()
root.style.theme_use('clam')
root.title('Sale Processing')

# Grid setup so elements resize with window
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=3)
#root.grid_columnconfigure(3, weight=1)

root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=3)
root.grid_rowconfigure(3, weight=3)
root.grid_rowconfigure(4, weight=3)

# Label Creation
Label(root, anchor='center', text='SKU:').grid(row=0, column=0, sticky=EW)
Label(root, anchor='center', text='Items').grid(row=0, column=2, sticky=EW)
Label(root, anchor='center', text='Quantity:').grid(row=1, column=0, sticky=EW)
Label(root, anchor='center', text='Subtotal:').grid(row=4, column=0, sticky=EW)

# Entry Creation
Entry(root, textvariable='Enter SKU').grid(row=0, column=1, sticky=W)
Entry(root, textvariable='Enter Qt').grid(row=1, column=1, sticky=W)

# Button Creation
add_btn = Button(root, anchor='center', text='Add').grid(row=2, column=0, sticky=NSEW)
total_btn = Button(root, anchor='center', text='Total').grid(row=3, column=0, sticky=NSEW)
back_btn = Button(root, anchor='center', text='Back').grid(row=2, column=1, sticky=NSEW)

root.mainloop()