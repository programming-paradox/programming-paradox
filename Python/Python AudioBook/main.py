from tkinter.filedialog import askopenfilename
import PyPDF2
from gtts import gTTS
import time

filelocation = askopenfilename()  # open the dialog GUI

string_of_text = ''

with open(filelocation, 'rb') as f:
    read_pdf = PyPDF2.PdfFileReader(f)
    number_of_pages = read_pdf.getNumPages()
    a = read_pdf.getPage(98)
    print(a.extractText())
