import pdfquery


class PDFReader:
    _pdf = None
    _width = 0
    _height = 0

    @classmethod
    def get_pdf(cls):
        return cls._pdf
    
    @classmethod
    def get_width(cls):
        return cls._width
    
    @classmethod
    def get_height(cls):
        return cls._height

    @classmethod
    def load_pdf(cls, path):
        try:
            cls._pdf = pdfquery.PDFQuery(path)
            cls._pdf.load()

            full_page = cls._pdf.pq('LTPage[pageid="1"]')
            cls._width = float(full_page.attr('width'))
            cls._height = float(full_page.attr('height'))
            return cls._pdf
        except Exception:
            return None
