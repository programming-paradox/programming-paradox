from tkinter.filedialog import askopenfilename
import PyPDF2
from gtts import gTTS
import time

filelocation = askopenfilename()  # open the dialog GUI

string_of_text = ''

with open(filelocation, 'rb') as f:
    read_pdf = PyPDF2.PdfFileReader(f)
    number_of_pages = read_pdf.getNumPages()
    for item in range(22, number_of_pages):
        page = read_pdf.getPage(item)
        page_content = page.extractText()
        string_of_text += page_content

time.sleep(10)
final_file = gTTS(text=string_of_text, lang='en')
final_file.save("Generated Speech.mp3")
