from tkinter import *
from datetime import date 

#importing font
#import pyglet
#pyglet.font.add_file('font name')

bc = "#ffffff"
fc = "#e34646"

#window configuration
window = Tk()
window.title("Digital Clock")
window.geometry('485x180')
window.resizable(width=False, height=False)
window.configure(bg=bc)

 def clock(): 
  time = datetime.now  
  hour = time.strftime("%H : %M : %S)
  print(hour)



l1 = Label(window, text = "12:49:05", font=('Arial 80'), bg=bc)
l1.grid(row = 0, column = 0, padx = 5, sticky = NW)

l2 = Label(window, text = "Wednesday 04/01/2023", font=('Arial 20'), bg=bc)
l2.grid(row = 1, column = 0, padx = 5, sticky = NW)

window.mainloop()