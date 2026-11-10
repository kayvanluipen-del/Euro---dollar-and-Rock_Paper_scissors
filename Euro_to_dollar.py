from tkinter import *

Gui_temp = Tk()
Gui_temp.config(background="white")
Gui_temp.title("Money")
Gui_temp.geometry("600x400")
def convert():
    Euro = Input_Euro.get()
    Euro_converter = (float(Euro)*1.12)
    output_Dollar.config(text="Money in Dollar   :" + str(Euro_converter))
Input_Euro = Entry()
title_label = Label(Gui_temp, text="Euro -> Dollar",bg= "white",fg= "black")
input_label = Label(Gui_temp, text= "Enter amount in Euro   :",bg= "White", fg= "black")
output_Dollar = Label(Gui_temp)
convert_button = Button(Gui_temp, text= "convert",width= 30, bg= "red", fg= "black", padx= 20, pady=10, command=convert)


title_label.grid(row=0,column=0)
input_label.grid(row=1,column=0)
Input_Euro.grid(row=1,column=1)
output_Dollar.grid(row=3,column=0)
convert_button.grid(row=4,column=0)



Gui_temp.mainloop()