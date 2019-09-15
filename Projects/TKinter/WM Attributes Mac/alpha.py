import tkinter as tk
form =tk.Tk()
form.title('Opacity')
form.geometry('300x300')
#? alpha double
#? controls opacity (from 0.0 to 1.0)
form.wm_attributes('-alpha','0.80')
tk.mainloop()