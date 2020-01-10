from PyPDF2 import PdfFileReader
from PyPDF2.utils import PdfReadError

class PDFReader():
    def run(self, file):
        input1 = PdfFileReader(file)
        try:
            numPages = input1.getNumPages()    
        except PdfReadError as err:
            raise PdfReadError(f"O arquivo {file} está protegido com senha. \n {err}")

        pages = ''
        for i in range(0, numPages):
            page = input1.getPage(i)
            pageText = page.extractText()
            pages += pageText

        return pages