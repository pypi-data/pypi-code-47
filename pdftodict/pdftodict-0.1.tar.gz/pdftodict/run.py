from app import PDFScrapper


if __name__ == "__main__":
    pdf_path_1 = './excel_examples/i002_bizfile-businessprofile(business)wcertofprod.pdf'
    pdf_path_2 = './excel_examples/i004_bizfile-businessprofile(company)withcertofprod.pdf'

    app = PDFScrapper()
    app.start(
        path=pdf_path_1
    )
