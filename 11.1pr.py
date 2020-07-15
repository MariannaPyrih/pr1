import tkinter as tk
from tkinter import filedialog as fd

def LoadFile(e):
    filename = fd.askopenfilename(filetypes=[('*.txt files', '.txt')])
    if not filename:
        return
    with open(filename, 'r', encoding='utf-8') as f:
        textbox.delete('1.0', 'end')
        textbox.insert('1.0', f.read())


def SaveFile(e):
    filename = fd.asksaveasfilename(filetypes=[('*.txt files', '.txt')])
    if not filename:
        return
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(textbox.get('1.0', 'end'))
      
 

root = tk.Tk()
panelFrame = tk.Frame(root, height=20, bg='blue')
textFrame = tk.Frame(root, height=40, width=50)
panelFrame.pack(side='top', fill='x')
textFrame.pack(side='bottom', fill='both', expand=1)
textbox = tk.Text(textFrame, font='Arial 12', wrap='word')
scrollbar = tk.Scrollbar(textFrame)
scrollbar['command'] = textbox.yview
textbox['yscrollcommand'] = scrollbar.set
textbox.pack(side='left', fill='both', expand=1)
scrollbar.pack(side='right', fill='y')
loadBtn = tk.Button(panelFrame, text='Open')
loadBtn.bind("<Button-1>", LoadFile)
saveBtn = tk.Button(panelFrame, text='Save')
saveBtn.bind("<Button-1>", SaveFile)

loadBtn.place(x=10, y=1, width=40, height=20)
saveBtn.place(x=60, y=1, width=40, height=20)
root.mainloop()
