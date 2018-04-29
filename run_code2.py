from tkinter import *
import tkinter.messagebox
from io import StringIO

root = Tk()
root.geometry('800x500')
root.title("Run Python Code")
color = 'thistle'
color2 = 'plum'
root.configure(bg=color)
root.resizable(height=False, width=False)

def clear_python():
    python_code.delete('1.0', END)

def run_python():
    old_stdout = sys.stdout
    redirected_output = sys.stdout = StringIO()
    exec(python_code.get('1.0', END))
    sys.stdout = old_stdout
    tkinter.messagebox.showinfo('Result', redirected_output.getvalue())

top = Frame(root, width=800, height=50, bg=color2)
top.pack(side=TOP)

bottom = Frame(root, width=800, height=450, bg=color)
bottom.pack(side=BOTTOM)

btn_clear = Button(top, text='Clear', highlightbackground=color2, font=('times new roman', 20, 'bold'),
                    command=lambda : clear_python())
btn_clear.pack(side=TOP)
btn_run = Button(top, text='Run', highlightbackground=color2, font=('times new roman', 20, 'bold'),
                    command=lambda : run_python())
btn_run.pack(side=TOP)

python_code = Text(top, font=('times new roman', 20, 'bold'), bg=color)
python_code.pack(side=TOP)



root.mainloop()
