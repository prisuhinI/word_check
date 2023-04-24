from tkinter import *
from textblob import TextBlob

root = Tk()
root.title('Word Checker')
root.geometry('700x400')
root.config(background='#043927')


def check_word():
    word = enter_text.get()
    a = TextBlob(word)
    right = str(a.correct())

    cs = Label(root, text='Correct text is :', font=('Trebuchet MS', 20), bg='#043927', fg="#7179ba")
    cs.place(x=210, y=230)
    spell.config(text=right)


heading = Label(root, text='Word Checker', font=('Trebuchet MS', 30, 'bold'), bg='#043927', fg='#7179ba')
heading.pack(pady=(50, 0))

enter_text = Entry(root, justify='center', width=30, font=('poppins', 25), bg='white', border=2)
enter_text.pack(pady=10)
enter_text.focus()

button = Button(root, text='Check', font=('arial', 20, 'bold'), fg='#7179ba', bg='red', command=check_word)
button.pack(pady=(10, 0))

spell = Label(root, font=('Trebuchet MS', 20), bg='#043927', fg='#7179ba')
spell.place(x=370, y=230)

root.mainloop()
