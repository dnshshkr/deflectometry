
# importing the module tkinter
import tkinter as tk
  
# create main window (parent window)
root = tk.Tk()
  
# Label() it display box
# where you can put any text. 
txt = tk.Label(root,
               text="Welcome to GeekForGeeks",pady=50,padx=100)
  
# pack() It organizes the widgets
# in blocks before placing in the parent widget.
txt.pack()
  
# running the main loop
root.mainloop()