from email import message
from tkinter import messagebox
from setuptools import Command
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
import tkinter as tk
from tkinter.font import BOLD
from turtle import color, st, title

def summarize():
    stext.config(state='normal')
    summ.config(state='normal')
    story = stext.get('1.0','end').strip() #strip removes any space in the beginning and the end
    stopWords = set (stopwords.words ("english"))
    words = word_tokenize (story) #extract tokens from words and sentences
    freqTable = dict() #displays the frequencies of different categories

    for word in words:
        word = word.lower()
        if word in stopWords:
            continue
        if word in freqTable:
            freqTable[word] += 1
        else:
            freqTable[word] = 1
    sentences = sent_tokenize(story)
    sentenceValue = dict()
    for sentence in sentences:
        for word, freq in freqTable.items():
            if word in sentence.lower():
                if sentence in sentenceValue:
                    sentenceValue [sentence] += freq
                else:
                    sentenceValue [sentence] = freq
    sumValues = 0
    for sentence in sentenceValue:
        sumValues += sentenceValue[sentence]
    # Average value of a sentence from the original text
    average = int(sumValues / len (sentenceValue))
    # Storing sentences into our summary.
    global summary
    summary = ''

    for sentence in sentences:
        if (sentence in sentenceValue) and (sentenceValue [sentence] > (1.2 * average)):
            summary += " " + sentence
    #print (summary)
    summ.delete('1.0','end')
    summ.insert('1.0',summary)
    stext.config(state='disabled')
    summ.config(state='disabled')

def save():
            file = open('summary.txt', 'w')
            file.write(summary)
            file.close()
            tk.messagebox.showinfo(title=None,message='Summary was saved')   
            
root = tk.Tk()
root.title("Story Summary")
root.geometry('800x600')
root.config(bg='#262526')


#tlabel = tk.Label(root, text="Title")
#tlabel.config(fg='#f4f4f4', bg='#262526',font=("Helvetica", 12), padx=10,pady=5)
#tlabel.pack()

slabel = tk.Label(root, text="Enter the Story Text")
slabel.config(fg='#f4f4f4', bg='#262526',font=("Helvetica", 12), padx=10,pady=15)
slabel.pack()

stext = tk.Text(root, height=12, width=95)
stext.config(bg='#1e1e1e', fg='#f4f4f4')
stext.pack()

btn = tk.Button(root, text='SUMARIZE', width=60,height=1 ,bg="#1b1b1b",command=summarize)
btn.config(fg='#f4f4f4',font=("Helvetica", 12, BOLD), padx=10,pady=15, borderwidth=1)
btn.pack(pady= 10, padx= 15)

llabel = tk.Label(root, text="The Summarization")
llabel.config(fg='#f4f4f4', bg='#262526',font=("Helvetica", 12), padx=10,pady=5)
llabel.pack()

summ = tk.Text(root, height=8, width=95)
summ.config(state='disabled', bg='#1e1e1e', fg='#f4f4f4')
summ.pack()

btn2 = tk.Button(root, text='SAVE SUMMARY', width=30,height=2 ,bg="#1b1b1b",command=save)
btn2.config(fg='#f4f4f4',font=("Helvetica", 12, BOLD), padx=10,pady=5, borderwidth=1)
btn2.pack(pady= 10, padx= 5)



root.mainloop()