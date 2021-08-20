'''
Passwort Generator Gui
@Ely Schybol
@created on 11.11.2020
'''
from tkinter import *
from pwgen2 import magic
#-----------------------------
window = Tk()
window.title('Passwort-Generator')
window.configure(background='azure')
window.resizable(width=FALSE, height=FALSE)
#--------------------------------
label = Label(window, text='Passwort-Generator', width=20, height=2, fg='black', bg='azure')
label.grid(row=1,column=0)
#-------------------------------
#Outputfield
output_field = Text(window,width=20, height=1, bg='azure', fg='black')
output_field.grid(row=2, column=0)
#------------------------------
#funktion
def egg():
	output_field.delete('1.0' ,END)
	buffer = str(magic(18))
	output_field.insert(END, buffer)
#-------------------------------
#button
scramble=Button(window, text='scramble!', width=20, command=egg, fg='black', bg='azure')
scramble.grid(row=3,column=0)
#-------------------------------

window.mainloop()
