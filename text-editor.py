#!/usr/bin/python3.4

#Modules
from tkinter import *
from tkinter import scrolledtext
from tkinter import filedialog
import os

#Global objects
fileNames = []
fontStyle = ['Hevletica']
fontSize = ['14']

#Settings of Window
root = Tk()
root.title('Text-Editor')

#% screan for two Frames
menuFrame = Frame(root, height=30, bg='grey')
textFrame = Frame(root, height=340, width=600, bg='white')
menuFrame.pack(side='top', fill='x')
textFrame.pack(side='bottom', fill='both', expand=1)

#Created textbox
textBox = scrolledtext.ScrolledText(master=textFrame, font= 'Hevletica 14', wrap='word')
textBox.pack(side='left', fill='both', expand=1)

#Functions
def loadFile(ev):
    #Types of files , could be added
    typesFiles = [('*.txt files', '.txt'),('*.py files', '.py')]
    fn = filedialog.Open(root, filetypes =typesFiles).show()
    #Check `Are file have name?`
    if fn == '':
        return
    textBox.delete('1.0', 'end')
    #Append for list of fileNames, for F(saveFile) & Checking 'is name real'
    fileNames.append(fn)
    textBox.insert('1.0', open(fn, 'rt').read())

def saveFileAs(ev):
    typesFiles = [('*.txt files', '.txt'),('*.py files', '.py')]
    fn = filedialog.SaveAs(root, filetypes=typesFiles).show()
    if fn == '':
        return
    #Check *if file have type*
    dot=0
    for c in fn:
        if c == '.':
            dot=1
    if dot != 1:
        fn+=".txt"

    fileNames.append(fn)
    open(fn, 'wt').write(textBox.get('1.0', 'end'))

def saveFile(event):
    #Check 'is file created?'
    #After save it
    if len(fileNames)==0:
        saveFileAs(event)
    open(fileNames[-1], 'wt').write(textBox.get('1.0', 'end'))

def deleteAll(ev):
    #Delete name of file -> new file -> saveFile don`t works
    #Clean up screan
    del fileNames[:]
    textBox.delete('1.0', 'end')

def changeFont():
    #Use values from two list, and update option in textBox
    value = str(fontStyle[-1])+str(fontSize[-1])
    textBox.configure(font=value)

def changeFontStyle(ev):
    #This shit, catch object*font* , parsed and add to list
    font = ev.widget
    index = int(font.curselection()[0])
    value = font.get(index)
    fontStyle.append(value)
    changeFont()

def changeFontSize(ev):
    #This shit, catch object*font* , parsed and add to list
    font = ev.widget
    index = int(font.curselection()[0])
    value = font.get(index)
    textBox.configure(font=value)
    fontSize.append(value)
    changeFont()

def settingsEditor(ev):
    #Window with settings
    root = Tk()
    root.title('Settings')
    root.geometry('185x190')

    #Created list with styles of fonts
    fontsListbox=Listbox(root, selectmode='BROWSE', name='fontsListbox')
    fontsListbox.place(x=10, y=10, width=135, height=160)
    fontsListbox.insert(END, '-'*35)
    fontsList = ["Comic ", "Courier ", "Arial ",
                 "Times ","Helvetica ", "Fixedsys ",
                 "Verdana ", "Ansi "]
    for item in fontsList:
        fontsListbox.insert(END, item)
    fontsListbox.bind('<<ListboxSelect>>', changeFontStyle)

    #Created list with sizes of fonts
    fontsSizeListbox=Listbox(root, selectmode='BROWSE')
    fontsSizeListbox.place(x=150, y=10, width=25, height=160)
    fontsSizeListbox.insert(END, '-'*5)
    fontsSizeList = ["8", "10", "12", "14", "16", "18", "20"]
    for item in fontsSizeList:
        fontsSizeListbox.insert(END, item)
    fontsSizeListbox.bind('<<ListboxSelect>>', changeFontSize)

    mainloop()

#Widgets and binds
saveAsButton = Button(menuFrame, text='Save As')
saveAsButton.bind('<Button-1>', saveFileAs)
saveAsButton.pack(side='left')

saveButton = Button(menuFrame, text='Save')
saveButton.bind('<Button-1>', saveFile)
saveButton.pack(side='left')
textBox.bind('<Control-s>', saveFile)

loadButton = Button(menuFrame, text='Load')
loadButton.bind('<Button-1>', loadFile)
loadButton.pack(side='left')

deleteButton = Button(menuFrame, text='Close')
deleteButton.bind('<Button-1>', deleteAll)
deleteButton.pack(side='left')

settingsButton = Button(menuFrame, text='Settings')
settingsButton.bind('<Button-1>', settingsEditor)
settingsButton.pack(side='left')


root.mainloop()
