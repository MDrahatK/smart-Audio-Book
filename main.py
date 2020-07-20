import pyttsx3
import PyPDF2
book = open('book.pdf','rb')
bookreader = PyPDF2.PdfFileReader(book)
pages = bookreader.numPages
print(pages)
mahi = pyttsx3.init()
page = bookreader.getPage(0)
text = page.extractText()
mahi.say(text)
mahi.runAndWait()