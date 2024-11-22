import tkinter as tk

import wikipedia # type: ignore

bg_color = "#C9E3CC"
txt_color = "#424340"

#---------------------------------------------------------------------------#

# Create a new instance of Tkinter
root = tk.Tk()

# cofig the window
root.title("guugle")
root.configure(background=bg_color)

#---------------------------------------------------------------------------#

def on_button_click():
  user_input = text_box.get()
  text_box.delete(0, tk.END)
  result_box.delete(1.0, tk.END)
  result_box.insert(tk.END, wikipedia.summary(user_input, sentences=2))

def truc_stilé():
  user_input = text_box.get()
  if (user_input == ""):
    text_box.delete(0, tk.END)
    text_box.insert(0, "rechercher")

#--------------------------------------------------------------------------#  

#define all of the elements of the window

button = tk.Button(root,text="rechercher",
                   command=on_button_click,
                   bg="#606C5A",
                   borderwidth=0,
                   highlightcolor="#B0B9A8",
                   fg=txt_color)

text_box = tk.Entry(root, bg="#B0B9A8",
                    borderwidth=2,
                    highlightcolor="#B0B9A8",
                    fg=txt_color)

result_box = tk.Text(root, 
                     height=5, 
                     width=55, 
                     bg="#B0B9A8", 
                     font=("Courier", 10), 
                     fg=txt_color)

#---------------------------------------------------------------------------#

#code in

root.bind('<Return>', lambda event: on_button_click())
truc_stilé()

#---------------------------------------------------------------------------#

#paste all the elements of the window

button.pack()

text_box.pack()

result_box.pack()

#---------------------------------------------------------------------------#

# Run the Tkinter main event loop
root.mainloop()
