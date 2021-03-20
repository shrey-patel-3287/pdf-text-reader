#install gtts module
#install PyPDF2 module (pip install PyPDF2)
from gtts import gTTS 
import os 
import PyPDF2

pdf=input('enter pdf path: ')
a=PyPDF2.PdfFileReader(pdf)
print('document info: ')
print(a.documentInfo)
no=a.getNumPages()
print('total pages: ')
print(no)
print('\n -converting to audio-')
start=input('from page number:')
to=input('to page number:')
for i in range(start,to):
    string += a.getPage(i).extractText()

with open("text.txt","w",encoding='utf-8') as f:
    f.write(string)
print(string)
language = 'en'
myobj = gTTS(text=string, lang=language, slow=False)
myobj.save("book.mp3") 
print('mp3 is ready....') 